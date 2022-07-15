from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import tiempo_carro as FormularioCarro, descartes as FormularioDescartes
from .models import tiempo_de_carro as ModeloCarro, control_de_descartes as ModeloControlDescartes

@login_required(login_url='/login')
def inicio(request):
    return render(request,'lentes/index.html',{})




def tiempo_de_carro(request):
    datos=ModeloCarro.objects.all()
    formulario=FormularioCarro
    if request.method=='POST':
        formulario=FormularioCarro(request.POST  or None, request.FILES or None)
        if formulario.is_valid():
            data=formulario.cleaned_data            
            formulario.save()    
            return redirect('/lentes/tiempo_de_carro')
    print(datos)
    return render(request,'lentes/tiempocarro.html',{'formulario':formulario,
                                                      'datos':datos})



def control_de_descartes(request):
    formulario_descartes=FormularioDescartes()
    if request.method=='POST':
        formulario_descartes=FormularioDescartes(request.POST  or None, request.FILES or None)
        if formulario_descartes.is_valid():
            formulario_descartes.save()
            return redirect('/lentes/')
    return render(request,'lentes/descarte.html',{'formulario_descartes':formulario_descartes})




def fin_o_p(request):
    return render(request,'lentes/finop.html',{})



def calculo_1():
    modelo=ModeloCarro()
    proceso=modelo.tipo_proceso['Hc']
    lente=modelo.tipo_lente['Argon']
    tiempo_ciclo=modelo.tiempo_ciclo

    if proceso == 'Hc' and lente == 'Argon':
        print('entramos')

