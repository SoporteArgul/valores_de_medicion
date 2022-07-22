from django.db import models
from django.utils import timezone

proceso_status=(('hc','Hc'),('af','Af'))
lente_status=[('argon','Argon'),('ecoline','Ecoline'),('mig','Mig'),('fall dual','Fall dual'),('argon elite','Argon Elite'),('neon','Neon'),('new classic','New classic'),('aviator','Aviator')]
lente_tipo=[('argon','Argon'),('ecoline','Ecoline'),('mig','Mig'),('neon','Neon')]
turno_trabajo=[('mañana','Mañana'),('tarde','Tarde'),('noche','Noche')]


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

    turno= models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=turno_trabajo,
        default='mañana',
        )
    
    fecha_hora=models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now()
        )


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
            default=None,
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
       
        piezas_buenas=models.CharField(
            max_length=10,
            default=None,
            null=False,  
            blank=False
        )
        piezas_malas=models.CharField(
            max_length=10,
            default=None,
            null=False,  
            blank=False
        )
        piezas_descartadas=models.CharField(
            max_length=10,
            default=None,
            null=False,  
            blank=False
        )

        turno= models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=turno_trabajo,
        default='mañana',
        )
    
        fecha_hora=models.DateTimeField(
            blank=False,
            null=False,
            default=timezone.now()
        )
        
        class Meta:
            db_table = 'control_de_descartes'
        



class  fin_de_op(models.Model):
    
    tipo_proceso=models.CharField(
        null=False,
        blank=False,
        choices=proceso_status,
        default=None,
        max_length=2
    )
    tipo_lente=models.CharField(
        max_length=12,
        null=False,
        blank=False,
        choices=lente_status,
        default=None
    )
    cant_rotulos=models.IntegerField(
        default=None,
        null=False,  
        blank=False
    )
    piezas_por_caja=models.IntegerField(
        default=None,
        null=False,  
        blank=False
    )
    carros=models.IntegerField(
        default=None,
        null=False,  
        blank=False
    )
    turno= models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=turno_trabajo,
        default='mañana',
        )
    
    fecha_hora=models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now()
        )

    class Meta:
        db_table = 'fin de operacion'