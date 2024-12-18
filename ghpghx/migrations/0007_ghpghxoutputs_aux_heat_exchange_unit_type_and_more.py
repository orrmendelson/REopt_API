# Generated by Django 4.0.7 on 2023-03-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghpghx', '0006_alter_ghpghxinputs_is_hybrid_ghx'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghpghxoutputs',
            name='aux_heat_exchange_unit_type',
            field=models.TextField(blank=True, help_text='Specifies if the auxiliary heat exchange unit is a heater or cooler', null=True),
        ),
        migrations.AlterField(
            model_name='ghpghxinputs',
            name='is_hybrid_ghx',
            field=models.BooleanField(blank=True, default=True, help_text='If the GHP system uses a hybrid GHX with auxiliary heater or cooler', null=True),
        ),
    ]
