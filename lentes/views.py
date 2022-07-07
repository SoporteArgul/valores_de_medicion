from django.shortcuts import render
from .forms import LentesForm
from .models import Lentes
# Create your views here.


def cargar_lentes(request):
   if request.method == "POST":
        form = LentesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
   else:
        form = LentesForm()
   return render(request, 'lentes/lentes.html', {'form':form})

def actualizar_lentes(request):
    pass

def mostrar_lentes(request):
     lentes = Lentes.objects.all()
     return render(request,'lentes/buscar.html',{'Lentes':lentes} )

def eliminar_lentes(request):
    pass