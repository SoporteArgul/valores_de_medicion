from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import tiempo_carro as carro
from .models import tiempo_de_carro as t_carro

@login_required(login_url='/login')
def inicio(request):
    return render(request,'lentes/index.html',{})




def tiempo_de_carro(request):
    if request.method=='POST':
        formulario=carro(request.POST) 
        if formulario.is_valid():
            print('llegue aca')
            data=formulario.cleanned_data     
            lentes=t_carro(
                tipo_proceso=data['tipo_proceso'],
                tipo_lente=data['tipo_lente'],
                tiempo_ciclo=data['tiempo_ciclo']
            )
            lentes.save()
    formulario=carro()
    return render(request,'lentes/tiempocarro.html',{'form':formulario})



def control_de_descartes(request):
    return render(request,'lentes/descarte.html',{})




def fin_o_p(request):
    return render(request,'lentes/finop.html',{})