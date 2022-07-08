# Generated by Django 4.0.4 on 2022-07-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LentesId', models.CharField(max_length=30)),
                ('Valor1', models.CharField(max_length=200)),
                ('Valor2', models.CharField(max_length=300)),
                ('Valor3', models.DateField()),
                ('Valor4', models.DateField()),
            ],
            options={
                'db_table': 'Lentes',
            },
        ),
    ]
