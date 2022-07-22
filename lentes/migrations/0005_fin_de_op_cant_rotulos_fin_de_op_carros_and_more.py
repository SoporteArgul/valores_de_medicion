# Generated by Django 4.0.4 on 2022-07-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0004_control_de_descartes_piezas_buenas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_de_op',
            name='cant_rotulos',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='fin_de_op',
            name='carros',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='fin_de_op',
            name='piezas_por_caja',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='fin_de_op',
            name='tipo_lente',
            field=models.CharField(choices=[('argon', 'Argon'), ('ecoline', 'Ecoline'), ('mig', 'Mig'), ('fall dual', 'Fall dual'), ('argon elite', 'Argon Elite'), ('neon', 'Neon'), ('new classic', 'New classic'), ('aviator', 'Aviator')], default=None, max_length=12),
        ),
        migrations.AddField(
            model_name='fin_de_op',
            name='tipo_proceso',
            field=models.CharField(choices=[('hc', 'Hc'), ('af', 'Af')], default=None, max_length=2),
        ),
    ]