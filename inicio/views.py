from django.http import HttpResponseRedirect  
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required(login_url='/login')
def inicio(request):
    return render(request,'inicio/index.html',{})

def login_request(request,*args, **kwargs):
    if (request.user.is_authenticated):
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get("username")
            password=request.POST.get("password")
            user_obj=authenticate(request,username=username,password=password)
            if user_obj is not None:
                login(request,user_obj)
                return HttpResponseRedirect('/',{})
            else:
                return render(request,'inicio/login.html',{'form':form,'msg':'Usuario o Contraseña incorrectos'})
        else:
            return render(request,'inicio/login.html',{'form':form,'msg':'Usuario o Contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request,'inicio/login.html',{'form':form})


def register_view(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect("/")
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login',{'msg':f'Usuario creado con exito {{username.upper}}'})
        else:
            return render(request,'inicio/singup.html',{'msg':'ERROR','form':form})
    else:
        form=UserRegistrationForm()   
    return render(request,'inicio/singup.html',{'form':form})

 
  


