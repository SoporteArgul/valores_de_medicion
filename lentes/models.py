from asyncio import Task
from cProfile import label
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
        )

    tipo_lente= models.CharField(
        max_length=12,
        null=False,blank=False,
        choices=lente_status,
        default='argon',
        )

    tiempo_ciclo=models.IntegerField(
        
        blank=False,
        null=True
    )
      
    tiempo_carro=models.CharField(
        max_length=50,
        default = None,
        null=True)

    class Meta:
        db_table = 'tiempo_de_carro'





class control_de_descartes(models.Model):
        t_ant_caja_n=models.IntegerField(
            default="",
            null=False,  
            blank=False,
            
        )
        t_ant_cantidad_n=models.IntegerField(
            default="",
            null=False,  
            blank=False,
            
        )
        t_act_caja_n=models.IntegerField(
            default="",
            null=False,  
            blank=False
        )
        t_act_cantidad_n=models.IntegerField(
            default="",
            null=False,  
            blank=False
        )
        piezas_por_caja=models.IntegerField(
            default="",
            null=False,  
            blank=False
        )
        peso_en_kg=models.IntegerField(
            default=0,
            null=False,  
            blank=False
        )
        tipo_lente=models.CharField(
            max_length=12,
            null=False,  
            blank=False,
            choices=lente_tipo,
            default='argon',
            verbose_name= 'Tipo de lente'
        )

        class Meta:
            db_table = 'control_de_descartes'
        

class  fin_de_op(models.Model):
    tipo_proceso=CharField()
    tipo_lente=CharField()
    cant_rotulos=IntegerField()
    piezas_por_caja=IntegerField()
