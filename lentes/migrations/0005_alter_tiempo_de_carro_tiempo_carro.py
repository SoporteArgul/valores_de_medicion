# Generated by Django 4.0.6 on 2022-07-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0004_alter_tiempo_de_carro_tiempo_carro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_de_carro',
            name='tiempo_carro',
            field=models.IntegerField(default=None, null=False),
        ),
    ]
