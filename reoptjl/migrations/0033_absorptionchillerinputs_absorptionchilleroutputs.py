# Generated by Django 4.0.7 on 2023-04-05 21:53

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reoptjl.models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0032_outageoutputs_chp_curtailed_series_kw_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsorptionChillerInputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='AbsorptionChillerInputs', serialize=False, to='reoptjl.apimeta')),
                ('thermal_consumption_hot_water_or_steam', models.TextField(blank=True, choices=[('steam', 'Steam'), ('hot_water', 'Hot Water')], help_text='Boiler thermal production type, hot water or steam', null=True)),
                ('installed_cost_per_ton', models.FloatField(blank=True, help_text='Thermal power-based cost of absorption chiller [$/ton] (3.5 ton to 1 kWt)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('min_ton', models.FloatField(blank=True, default=0.0, help_text='Minimum thermal power size constraint for optimization [ton]', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('max_ton', models.FloatField(blank=True, default=100000000.0, help_text='Maximum thermal power size constraint for optimization [ton]', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('cop_thermal', models.FloatField(blank=True, help_text='Absorption chiller system coefficient of performance - conversion of hot thermal power input to usable cooling thermal energy output', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('cop_electric', models.FloatField(blank=True, default=14.1, help_text='Absorption chiller electric consumption CoP from cooling tower heat rejection - conversion of electric power input to usable cooling thermal energy output', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('om_cost_per_ton', models.FloatField(blank=True, help_text='Yearly fixed O&M cost [$/ton]', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('macrs_option_years', models.IntegerField(blank=True, choices=[(0, 'Zero'), (5, 'Five'), (7, 'Seven')], default=0, help_text='Duration over which accelerated depreciation will occur. Set to zero to disable')),
                ('macrs_bonus_fraction', models.FloatField(blank=True, default=0.0, help_text='Percent of upfront project costs to depreciate in year one in addition to scheduled depreciation', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
            ],
            bases=(reoptjl.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='AbsorptionChillerOutputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='AbsorptionChillerOutputs', serialize=False, to='reoptjl.apimeta')),
                ('size_kw', models.FloatField(blank=True, help_text='Thermal power capacity of the absorption chiller [kW]', null=True)),
                ('size_ton', models.FloatField(blank=True, help_text='Thermal power capacity of the absorption chiller [ton]', null=True)),
                ('thermal_to_storage_series_ton', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of absorption chiller thermal to cold TES [Ton]', null=True, size=None)),
                ('thermal_to_load_series_ton', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of absorption chiller thermal to cooling load [Ton]', null=True, size=None)),
                ('thermal_consumption_series_mmbtu_per_hour', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of absorption chiller electric consumption [kW]', null=True, size=None)),
                ('annual_thermal_consumption_mmbtu', models.FloatField(blank=True, help_text='Year one absorption chiller electric consumption [kWh]', null=True)),
                ('annual_thermal_production_tonhour', models.FloatField(blank=True, help_text='Year one absorption chiller thermal production [Ton Hour', null=True)),
                ('electric_consumption_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of absorption chiller electric consumption [kW]', null=True, size=None)),
                ('annual_electric_consumption_kwh', models.FloatField(blank=True, help_text='Year one absorption chiller electric consumption [kWh]', null=True)),
            ],
            bases=(reoptjl.models.BaseModel, models.Model),
        ),
    ]
