# Generated by Django 4.0.6 on 2022-07-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0013_remove_tiempo_de_carro_tiempo_carro'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiempo_de_carro',
            name='tiempo_carro',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
