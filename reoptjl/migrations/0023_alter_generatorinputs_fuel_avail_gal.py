# Generated by Django 4.0.4 on 2023-03-07 22:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0022_merge_20230114_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatorinputs',
            name='fuel_avail_gal',
            field=models.FloatField(blank=True, default=1000000000.0, help_text='On-site generator fuel available in gallons per year.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
    ]