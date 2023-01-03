# Generated by Django 4.0.4 on 2022-12-21 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0009_erpgeneratorinputs_erpprimegeneratorinputs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='erpprimegeneratorinputs',
            name='prime_mover',
            field=models.TextField(choices=[('recip_engine', 'Recip Engine'), ('micro_turbine', 'Micro Turbine'), ('combustion_turbine', 'Combustion Turbine'), ('fuel_cell', 'Fuel Cell')], default='recip_engine', help_text='Prime generator/CHP prime mover, one of recip_engine, micro_turbine, combustion_turbine, fuel_cell'),
        ),
        migrations.AlterField(
            model_name='erpgeneratorinputs',
            name='failure_to_start',
            field=models.FloatField(blank=True, default=0.0066, help_text='Chance of generator not starting when an outage occurs', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='failure_to_run',
            field=models.FloatField(blank=True, help_text='Chance of CHP unit failing in each hour of outage', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='failure_to_start',
            field=models.FloatField(blank=True, default=0, help_text='Chance of CHP unit not starting when an outage occurs', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='operational_availability',
            field=models.FloatField(blank=True, help_text='Fraction of year CHP units are not down for maintenance', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]