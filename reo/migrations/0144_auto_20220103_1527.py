# Generated by Django 3.1.14 on 2022-01-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0143_auto_20220103_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rcmodel',
            old_name='wh_comfort_cost_total',
            new_name='hvac_comfort_cost_total',
        ),
    ]