# Generated by Django 4.0.6 on 2022-07-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0002_control_de_descartes_peso_en_kg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_de_carro',
            name='tiempo_carro',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
