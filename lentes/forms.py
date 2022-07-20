from dataclasses import fields
from django import forms
from .models import tiempo_de_carro,control_de_descartes,fin_de_op

class tiempo_carro(forms.ModelForm):  
      class Meta:
          widgets={
              'tipo_proceso': forms.Select(attrs={
                  'id':'proceso',
                  'class':'sidebar-box'}),
              'tipo_lente': forms.Select(attrs={
                  'id':'tipo',
                  'class':'sidebar-box'
                  
              }),
              'tiempo_ciclo': forms.NumberInput(attrs={
                  'id':'ciclo',
                  'class':'sidebar-box'}),
              'tiempo_carro':forms.TextInput(attrs={
                    'id':'resultado',
                    'name':'tiempoCarro',
                    'value':'',
                    'class':'sidebar-box'
              })
          }
          model=tiempo_de_carro
          fields=['tipo_proceso','tipo_lente','tiempo_ciclo','tiempo_carro'] 




"""class descartes(forms.ModelForm):
    class Meta:
        widgets={
        't_ant_caja_n': forms.NumberInput(attrs={
            'id':'caja1',
            }),
        't_ant_cantidad_n':forms.NumberInput(attrs={'id':'cant1'}),
        't_act_caja_n':forms.NumberInput(attrs={'id':'caja2'}),
        't_act_cantidad_n':forms.NumberInput(attrs={'id':'cant2'}),
        'piezas_por_caja':forms.NumberInput(attrs={'id':'piezasxcaja'}),
        'tipo_lente':forms.Select(attrs={'id':'tipolente'}),
        'peso_en_kg':forms.NumberInput(attrs={'id':'grs'})
        }
        model=control_de_descartes
        fields=['t_ant_caja_n','t_ant_cantidad_n','t_act_caja_n','t_act_cantidad_n','piezas_por_caja','tipo_lente','peso_en_kg']
"""

class descartes(forms.Form):
     t_ant_cantidad_n=forms.IntegerField(label='Turno anterior:')
     t_ant_cantidad_n=forms.IntegerField(label='')
     t_act_caja_n=forms.IntegerField(label='Turno actual:')
     t_act_cantidad_n=forms.IntegerField(label='')
     piezas_por_caja=forms.IntegerField(label='Piezas por caja:')
   
     peso_en_kg=forms.IntegerField(label='Peso en gramos')



class finop(forms.ModelForm):
    class Meta:
        model=fin_de_op
        fields='__all__'

    