# Generated by Django 3.1.12 on 2021-08-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0115_auto_20210810_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='chpmodel',
            name='supplementary_firing_efficiency',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chpmodel',
            name='supplementary_firing_max_steam_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
