from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

import lentes
from .forms import BusquedaControl, BusquedaFin, tiempo_carro as FormularioCarro, descartes as FormularioDescartes, finop as FormularioFinOp, BusquedaCarro
from .models import tiempo_de_carro as ModeloCarro, control_de_descartes as ModeloControlDescartes, fin_de_op as ModeloFinOp

@login_required(login_url='/login')
def inicio(request):
    return render(request,'lentes/index.html',{})




def tiempo_de_carro(request):
    formulario=FormularioCarro
    if request.method=='POST':
        formulario=FormularioCarro(request.POST  or None, request.FILES or None)
        if formulario.is_valid():
            data=formulario.cleaned_data 
            formulario.save()    
            return redirect('/lentes/tiempo_de_carro')
    return render(request,'lentes/tiempocarro.html',{'formulario':formulario,})



def control_de_descartes(request):
    formulario=FormularioDescartes()
    if request.method=='POST':
        formulario=FormularioDescartes(request.POST  or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lentes/control_de_descartes')
    return render(request,'lentes/descarte.html',{'formulario':formulario})


def fin_o_p(request):
    formulario=FormularioFinOp()
    if request.method=='POST':
        formulario=FormularioFinOp(request.POST  or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lentes/fin_op')
    return render(request,'lentes/finop.html',{'formulario':formulario})

def tabla_tiempo_de_carro(request):
    if request.method== 'GET':
        datos=ModeloCarro.objects.all()
    elemento_buscado=[]
    dato=request.GET.get('busqueda_carro',None)
    if dato is not None:
       elemento_buscado=ModeloCarro.objects.filter(turno__icontains=dato)
       
    buscador=BusquedaCarro()  
    return render(request,'lentes/listado_tiempo_de_carro.html',{ 'elemento_buscado':elemento_buscado,
                                                                  'buscador':buscador,
                                                                  'dato':dato,
                                                                  'datos':datos
                                                                })
def tabla_control_de_descartes(request):
     if request.method== 'GET':
        datos=ModeloControlDescartes.objects.all()
     elemento_buscado=[]
     dato=request.GET.get('busqueda_carro',None)
     if dato is not None:
       elemento_buscado=ModeloControlDescartes.objects.filter(turno__icontains=dato)
       
     buscador=BusquedaControl()  
     return render(request,'lentes/listado_control_descartes.html',{ 'elemento_buscado':elemento_buscado,
                                                                  'buscador':buscador,
                                                                  'dato':dato,
                                                                  'datos':datos
                                                                })

def tabla_fin_op(request):
     if request.method== 'GET':
        datos=ModeloFinOp.objects.all()
     elemento_buscado=[]
     dato=request.GET.get('busqueda_carro',None)
     if dato is not None:
       elemento_buscado=ModeloFinOp.objects.filter(turno__icontains=dato)
       
     buscador=BusquedaFin()  
     return render(request,'lentes/listado_tiempo_de_carro.html',{ 'elemento_buscado':elemento_buscado,
                                                                  'buscador':buscador,
                                                                  'dato':dato,
                                                                  'datos':datos
                                                                })
     
   

