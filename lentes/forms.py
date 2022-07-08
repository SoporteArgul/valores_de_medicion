from dataclasses import fields
from django import forms


class tiempo_carro(forms.Form):  
      tipo_proceso=forms.CharField(
          max_length=3,)
      tipo_lente=forms.CharField(
          max_length=12,)
      tiempo_ciclo=forms.IntegerField()      

        
        