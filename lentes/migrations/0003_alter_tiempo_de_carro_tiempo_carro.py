# Generated by Django 4.0.6 on 2022-07-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0002_remove_tiempo_de_carro_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_de_carro',
            name='tiempo_carro',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
