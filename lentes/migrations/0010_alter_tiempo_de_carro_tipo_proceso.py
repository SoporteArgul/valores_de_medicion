# Generated by Django 4.0.4 on 2022-07-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0009_alter_tiempo_de_carro_tipo_proceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_de_carro',
            name='tipo_proceso',
            field=models.IntegerField(choices=[('Hc', 'hc'), ('Af', 'af')], default='Hc'),
        ),
    ]
