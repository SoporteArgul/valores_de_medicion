# Generated by Django 4.0.4 on 2022-07-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0005_fin_de_op_cant_rotulos_fin_de_op_carros_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiempo_de_carro',
            name='fecha_y_hora',
            field=models.TimeField(default=None),
        ),
    ]
