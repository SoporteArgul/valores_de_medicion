from pyexpat import model
from django.db import models

class Lentes(models.Model):
    LentesId = models.CharField(max_length=30)
    Valor1 = models.CharField(max_length=200)
    Valor2 = models.CharField(max_length=300)
    

  
    class Meta:
        db_table = 'Lentes'
