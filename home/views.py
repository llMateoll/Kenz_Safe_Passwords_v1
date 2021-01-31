from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Clave
from .forms import ClaveForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    clave = Clave.objects.all()

    form = ClaveForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request,'index.html', {'clave':clave, 'form':form, 'mensaje':'Success'})

@login_required(login_url='/accounts/login/')
def edit(request, clave_id):
    # Recuperamos la instancia de la persona
    instancia = Clave.objects.get(id=clave_id)

    # Creamos el formulario con los datos de la instancia
    form = ClaveForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ClaveForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

        return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "edit.html", {'form': form, 'instancia':instancia})

@login_required(login_url='/accounts/login/')
def delete(request, clave_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Clave.objects.get(id=clave_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/')


















# def AddClaves(request):
#     form = ClaveForm(request.POST)

#     if form.is_valid():
#         form.save()
    
#     return render(request,'index.html', {'form':form, 'mensaje':'Ok'})