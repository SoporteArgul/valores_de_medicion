from asyncio import Task
from django.db import models
from django.forms import CharField, IntegerField
from django import forms
from django.db.models import Sum


proceso_status=(('hc','Hc'),('af','Af'))
lente_status=[('argon','Argon'),('ecoline','Ecoline'),('mig','Mig'),('fall dual','Fall dual'),('argon elite','Argon Elite'),('neon','Neon'),('new classic','New classic'),('aviator','Aviator')]
lente_tipo=[('argon','Argon'),('ecoline','Ecoline'),('mig','Mig'),('neon','Neon')]



class tiempo_de_carro(models.Model):

    tipo_proceso = models.CharField(
        null=False,
        blank=False,
        choices=proceso_status,
        default='Hc',
        max_length=2,
        verbose_name='Tipo de proceso')

    tipo_lente= models.CharField(
        max_length=12,
        null=False,blank=False,
        choices=lente_status,
        default='argon',
        verbose_name= 'Tipo de lente')

    tiempo_ciclo=models.IntegerField(
        verbose_name='Tiempo de ciclo',
        blank=False,
        null=True
    )
    
    
    tiempo_carro=models.IntegerField(
        default = None,
        null=True)

    
        
          


    class Meta:
        db_table = 'tiempo_de_carro'





class control_de_descartes(models.Model):
        t_ant_caja_n=models.IntegerField()
        t_ant_cantidad_n=models.IntegerField()
        t_act_caja_n=models.IntegerField()
        t_act_cantidad_n=models.IntegerField()
        piezas_por_caja=models.IntegerField()
        tipo_lente=models.CharField(
            max_length=12,
            null=False,  
            blank=False,
            choices=lente_tipo,
            default='argon',
            verbose_name= 'Tipo de lente'
        )
        peso_en_kg=IntegerField()





class  fin_de_op(models.Model):
    tipo_proceso=CharField()
    tipo_lente=CharField()
    cant_rotulos=IntegerField()
    piezas_por_caja=IntegerField()
