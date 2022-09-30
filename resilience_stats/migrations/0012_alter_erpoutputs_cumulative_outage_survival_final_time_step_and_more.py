# Generated by Django 4.0.6 on 2022-09-28 17:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0011_alter_erpoutputs_mean_cumulative_outage_survival_final_time_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erpoutputs',
            name='cumulative_outage_survival_final_time_step',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='The probability of surviving the full max_outage_duration, for outages starting at each hour of the year.', size=None),
        ),
        migrations.AlterField(
            model_name='erpoutputs',
            name='mean_cumulative_survival_by_duration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='The mean, calculated over outages starting at each hour of the year, of the cumulative probability of surviving up to and including each hour of max_outage_duration.', size=None),
        ),
        migrations.AlterField(
            model_name='erpoutputs',
            name='mean_marginal_survival_by_duration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='The mean, calculated over outages starting at each hour of the year, of the marginal probability of surviving each hour of max_outage_duration.', size=None),
        ),
        migrations.AlterField(
            model_name='erpoutputs',
            name='min_cumulative_survival_by_duration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='The minimum, calculated over outages starting at each hour of the year, of the cumulative probability of surviving up to and including each hour of max_outage_duration.', size=None),
        ),
        migrations.AlterField(
            model_name='erpoutputs',
            name='min_marginal_survival_by_duration',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='The minimum, calculated over outages starting at each hour of the year, of the marginal probability of surviving each hour of max_outage_duration.', size=None),
        ),
    ]