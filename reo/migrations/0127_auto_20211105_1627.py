# Generated by Django 3.1.12 on 2021-11-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0126_auto_20211105_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitemodel',
            old_name='emissions_reduction_max_pct',
            new_name='co2_emissions_reduction_max_pct',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='emissions_reduction_min_pct',
            new_name='co2_emissions_reduction_min_pct',
        ),
    ]