# Generated by Django 4.0.4 on 2022-07-22 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0007_alter_tiempo_de_carro_fecha_y_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_de_carro',
            name='fecha_y_hora',
            field=models.TimeField(default=datetime.datetime(2022, 7, 22, 12, 15, 30, 360719, tzinfo=utc)),
        ),
    ]
