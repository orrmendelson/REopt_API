# REopt®, Copyright (c) Alliance for Sustainable Energy, LLC. See also https://github.com/NREL/REopt_API/blob/master/LICENSE.
from resilience_stats.outage_simulator_LF import simulate_outages
from resilience_stats.models import ResilienceModel
from reo.models import ScenarioModel
import numpy as np
import logging
log = logging.getLogger(__name__)


def calc_avoided_outage_costs(data, present_worth_factor, run_uuid):
    """
    Add output parameter to data:
        data['outputs']['Scenario']['Site']['avoided_outage_costs_us_dollars']
            = VoLL X avg_hrs_sustained X avg_crit_ld X present_worth_factor
    :param data: nested dict used for API response
    :param present_worth_factor: float, accounts for escalation and discount of avoided outage costs over analysis
        period. NOTE: we use pwf_e from REopt, which uses the electricity cost escalation rate and offtaker
        discount rate.
    :param run_uuid: UUID
    :return: None

    NOTE: we cannot use resilience_stats endpoint for this calculation because it relies on the results already being
    saved to the DB, and calculating the outage costs is done before the results are saved because it is one of the
    results.

    NOTE: this function saves the outage simulator results to the database to ensure that the simulation is not run
    twice (second time occurs when user calls resilience_stats endpoint with run_uuid).
    """
    site_inputs = data['inputs']['Scenario']['Site']
    site_outputs = data['outputs']['Scenario']['Site']
    pvs = site_outputs['PV']
    wind = site_outputs['Wind']
    chp_kw = site_outputs["CHP"]["size_kw"]

    load_profile = site_inputs['LoadProfile']
    batt_roundtrip_efficiency = site_inputs['Storage']['internal_efficiency_pct'] \
                                * site_inputs['Storage']['inverter_efficiency_pct'] \
                                * site_inputs['Storage']['rectifier_efficiency_pct']
    critical_load = site_outputs['LoadProfile']['critical_load_series_kw']

    """
    smishra 200515
    For enabling existing diesel generator for the financial scenario of resilience
    analysis, the following block is being added. Since the code-flow is same for 
    both financial and resilience scenarios in a resilience analysis, this block makes
    sure that existing_kw gets captured for financial case. For resilience scenario, 
    on the other hand, the generator sizing input to the simulate_outages function must 
    [capture existing_kw + new_capacity_kw ]
     
    Note: "generator_only_runs_during_grid_outage" is set to true by default
    """
    generator_in = site_inputs['Generator']
    generator_out = site_outputs['Generator']

    if generator_in["generator_only_runs_during_grid_outage"]:

        if load_profile.get('outage_start_time_step') is None and load_profile.get('outage_end_time_step') is None:
            # handles financial scenario where there will only be non-zero input kw
            diesel_kw_for_case = generator_in.get('existing_kw')

        elif load_profile.get('outage_start_time_step') is not None and load_profile.get('outage_end_time_step') is not None:
    # handles resilience scenarion where output will have existing_kw embedded
            diesel_kw_for_case = generator_out.get('size_kw')

    # works for financial scenario when the generator is allowed to run
    # year-long, which means model can recommend new generator capacity)
    else:
        diesel_kw_for_case = generator_out.get('size_kw')

    pv_production = []
    for p in pvs:
        add_prod = p.get('year_one_power_production_series_kw') or []
        if add_prod != []:
            if pv_production == []:
                pv_production = add_prod
            else:
                pv_production += np.array(add_prod)
    if sum(pv_production) == 0:
        pv_production = []

    celery_eager = True
    """ nlaws 200229
    Set celery_eager = False to run each inner outage simulator loop in parallel. Timing tests with generator only
    indicate that celery task management does not improve speed due to the overhead required to manage the 8760 tasks.
    However, if the outage simulator does get more complicated (say with CHP) we should revisit using celery to run
    the inner loops in parallel.
    try:
        if load_profile['outage_end_time_step'] - load_profile['outage_start_time_step'] > 1000:
            celery_eager = False
    except KeyError:
        pass  # in case no outage has been defined
    """
    results = simulate_outages(
        batt_kwh=site_outputs['Storage'].get('size_kwh') or 0,
        batt_kw=site_outputs['Storage'].get('size_kw') or 0,
        pv_kw_ac_hourly=list(pv_production),
        wind_kw_ac_hourly=wind['year_one_power_production_series_kw'],
        init_soc=site_outputs['Storage'].get('year_one_soc_series_pct'),
        critical_loads_kw=critical_load,
        batt_roundtrip_efficiency=batt_roundtrip_efficiency,
        diesel_kw=diesel_kw_for_case,
        fuel_available=generator_in['fuel_avail_gal'],
        b=generator_in['fuel_intercept_gal_per_hr'],
        m=generator_in['fuel_slope_gal_per_kwh'],
        celery_eager=celery_eager,
        chp_kw=chp_kw
    )

    avg_crit_ld = sum(critical_load) / len(critical_load)

    if load_profile['outage_is_major_event']:
        # assume that outage occurs only once in analysis period
        present_worth_factor = 1

    data['outputs']['Scenario']['Site']['Financial']['avoided_outage_costs_us_dollars'] = round(
        site_inputs['Financial']['value_of_lost_load_us_dollars_per_kwh']
        * results['resilience_hours_avg']
        * avg_crit_ld
        * present_worth_factor, 2)

    results.update({
        "present_worth_factor": present_worth_factor,
        "avg_critical_load": avg_crit_ld
    })
    # save results
    try:
        scenario = ScenarioModel.objects.get(run_uuid=run_uuid)
        rm = ResilienceModel.create(scenariomodel=scenario, **results)
    except:
        log.warning("Failed to save ResilienceModel for run_uuid {}".format(run_uuid))
    else:
        log.info("Successfully saved ResilienceModel for run_uuid {}".format(run_uuid))
