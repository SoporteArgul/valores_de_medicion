from django.db import models


proceso_status=(('hc','Hc'),('af','Af'))
lente_status=(('argon','Argon'),('ecoline','Ecoline'),('mig','Mig'),('fall dual','Fall dual'),('argon elite','Argon Elite'),('neon','Neon'),('neon classic','New classic'))

class tiempo_de_carro(models.Model):

    tipo_proceso = models.CharField(
        null=False,blank=False,
        choices=proceso_status,
        default='Hc',
        max_length=2)

    tipo_lente= models.CharField(
        null=False,blank=False,
        choices=lente_status,
        default='argon',
        max_length=12)

    tiempo_ciclo=models.IntegerField()
    

    class Meta:
        db_table = 'tiempo_de_carro'