from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import tiempo_de_carro as carro


@login_required(login_url='/login')
def inicio(request):
    return render(request,'lentes/index.html',{})




def tiempo_de_carro(request):
    form=carro()
    if request.method=='POST':
        form=carro(request.POST)      
        form.save()
    return render(request,'lentes/tiempocarro.html',{'form':form})



def control_de_descartes(request):
    return render(request,'lentes/descarte.html',{})




def fin_o_p(request):
    return render(request,'lentes/finop.html',{})