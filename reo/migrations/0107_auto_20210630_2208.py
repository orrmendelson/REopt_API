# Generated by Django 3.1.12 on 2021-06-30 22:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0106_auto_20210630_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='boilermodel',
            name='emissions_factor_lb_PM_per_mmbtu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boilermodel',
            name='year_one_emissions_bau_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boilermodel',
            name='year_one_emissions_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chpmodel',
            name='emissions_factor_lb_PM_per_mmbtu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chpmodel',
            name='year_one_emissions_bau_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chpmodel',
            name='year_one_emissions_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='emissions_factor_series_lb_PM_per_kwh',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_bau_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='emissions_factor_lb_PM_per_gal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_emissions_bau_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_emissions_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_bau_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_lb_PM',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
