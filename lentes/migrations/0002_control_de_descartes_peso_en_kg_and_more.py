# Generated by Django 4.0.6 on 2022-07-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='control_de_descartes',
            name='peso_en_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='control_de_descartes',
            name='piezas_por_caja',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='control_de_descartes',
            name='t_act_caja_n',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='control_de_descartes',
            name='t_act_cantidad_n',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='control_de_descartes',
            name='t_ant_caja_n',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='control_de_descartes',
            name='t_ant_cantidad_n',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterModelTable(
            name='control_de_descartes',
            table='control_de_descartes',
        ),
    ]
