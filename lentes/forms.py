from dataclasses import fields
from django import forms
from .models import tiempo_de_carro,control_de_descartes,fin_de_op

class tiempo_carro(forms.ModelForm):  
      class Meta:
          tipo_proceso=forms.CharField(widget=forms.TextInput(attrs={
              "class":"proceso"
          }))
          
          tipo_lente=forms.CharField(widget=forms.TextInput(attrs={
              "class":"tipo"
          }))

          tiempo_ciclo=forms.CharField(widget=forms.TextInput(attrs={
            "class":'input',
            "placeholder":'0'
          }))
          model=tiempo_de_carro
          fields=['tipo_proceso','tipo_lente','tiempo_ciclo'] 
     
class descartes(forms.ModelForm):
    class Meta:
        model=control_de_descartes
        fields='__all__'
    
class finop(forms.ModelForm):
    class Meta:
        model=fin_de_op
        fields='__all__'

    