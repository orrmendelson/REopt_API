# Generated by Django 4.0.7 on 2023-03-10 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0149_ghpmodel_aux_cooler_energy_use_intensity_kwe_per_kwt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghpmodel',
            name='is_hybrid_ghx',
        ),
    ]