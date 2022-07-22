from dataclasses import fields
from django import forms
from .models import tiempo_de_carro,control_de_descartes,fin_de_op

class tiempo_carro(forms.ModelForm):  
      class Meta:
          widgets={
              'tipo_proceso': forms.Select(attrs={
                  'id':'proceso',
                  'class':'sidebar-box'
                }),
              'tipo_lente': forms.Select(attrs={
                  'id':'tipo',
                  'class':'sidebar-box'   
              }),
              'turno':forms.Select(attrs={
                'id':'sidebar-box' 
              }),
              'tiempo_ciclo': forms.NumberInput(attrs={
                  'id':'ciclo',
                  'class':'sidebar-box'
            }),
              'tiempo_carro':forms.TextInput(attrs={
                    'id':'resultado',
                    'name':'tiempoCarro',
                    'value':'',
                    'class':'sidebar-box oculto'
              })
          }
          model=tiempo_de_carro
          fields=['tipo_proceso','tipo_lente','turno','tiempo_ciclo','tiempo_carro'] 




class descartes(forms.ModelForm):
    class Meta:
        widgets={
        't_ant_caja_n': forms.NumberInput(attrs={
            'id':'caja1',
            }),
        't_ant_cantidad_n':forms.NumberInput(attrs={
            'id':'cant1',
            }),
        't_act_caja_n':forms.NumberInput(attrs={
            'id':'caja2'
        }),
        't_act_cantidad_n':forms.NumberInput(attrs={
            'id':'cant2'
            }),
        'piezas_por_caja':forms.NumberInput(attrs={
            'id':'piezasxcaja'
            }),
        'tipo_lente':forms.Select(attrs={
            'id':'tipolente'
            }),
        'peso_en_kg':forms.NumberInput(attrs={
            'id':'grs'
            }),
        'piezas_descartadas':forms.NumberInput(attrs={
            'id':'scrap',
            'value':''
        }),
        'piezas_buenas':forms.NumberInput(attrs={
            'id':'buenas',
            'value':''

        }),
        'piezas_malas':forms.NumberInput(attrs={
            'id':'malas',
            'value':''
        }),
        'turno':forms.Select()

        }
        model=control_de_descartes
        fields=['t_ant_caja_n','t_ant_cantidad_n','t_act_caja_n','t_act_cantidad_n','piezas_por_caja','tipo_lente','peso_en_kg','turno','piezas_descartadas','piezas_malas','piezas_buenas']





class finop(forms.ModelForm):
    class Meta:
        widgets={
            'tipo_proceso':forms.Select(
                attrs={
                    'id':'proceso'
                }),
            'tipo_lente':forms.Select(
                attrs={
                    'id':'tipo'
                }),
            'cant_rotulos':forms.NumberInput(
                attrs={
                    'id':'rotulos'
                }),
            'piezas_por_caja':forms.NumberInput(
                attrs={
                    'id':'piezas'
                }),
            'carros':forms.NumberInput(
                attrs={
                    'id':'resultado',
                    'name':'finOp',
                    'value':'',
                    'class':'sidebar-box '
                }),
            'turno':forms.Select()
        }
        model=fin_de_op
        fields=['tipo_proceso','tipo_lente','cant_rotulos','piezas_por_caja','turno','carros']



class BusquedaCarro(forms.Form):
    busqueda_carro=forms.CharField(label='Buscador',max_length=20)


class BusquedaControl(forms.Form):
    busqueda_control=forms.CharField(label='Buscador',max_length=20)


class BusquedaFin(forms.Form):
    busqueda_fin=forms.CharField(label='Buscador',max_length=20)