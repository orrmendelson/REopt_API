from django.contrib import admin
from .models import URDBError, ProfileModel, ScenarioModel, SiteModel, FinancialModel, LoadProfileModel, LoadProfileBoilerFuelModel

@admin.register(URDBError)
class URDBErrorAdmin(admin.ModelAdmin):
    list_display = ('label', 'type', 'message')
    search_fields = ('label', 'type', 'message')

@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid', 'pre_setup_scenario_seconds', 'setup_scenario_seconds', 'reopt_seconds')
    search_fields = ('run_uuid',)

@admin.register(ScenarioModel)
class ScenarioModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid', 'api_version', 'user_uuid', 'webtool_uuid', 'job_type', 'description', 'status')
    search_fields = ('run_uuid', 'user_uuid', 'webtool_uuid', 'job_type', 'description', 'status')

@admin.register(SiteModel)
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid', 'address', 'latitude', 'longitude', 'land_acres', 'roof_squarefeet')
    search_fields = ('run_uuid', 'address')

@admin.register(FinancialModel)
class FinancialModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid', 'analysis_years', 'escalation_pct', 'generator_fuel_escalation_pct')
    search_fields = ('run_uuid',)

@admin.register(LoadProfileModel)
class LoadProfileModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid', 'doe_reference_name', 'annual_kwh', 'year')
    search_fields = ('run_uuid', 'doe_reference_name')

@admin.register(LoadProfileBoilerFuelModel)
class LoadProfileBoilerFuelModelAdmin(admin.ModelAdmin):
    list_display = ('run_uuid',)
    search_fields = ('run_uuid',)