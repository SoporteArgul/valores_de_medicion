from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import tiempo_carro as FormularioCarro, descartes as FormularioDescartes, finop as FormularioFinOp
from .models import tiempo_de_carro as ModeloCarro, control_de_descartes as ModeloControlDescartes, fin_de_op as ModeloFinOp

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





