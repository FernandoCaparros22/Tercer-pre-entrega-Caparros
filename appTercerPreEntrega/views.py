from django.shortcuts import render
from django.http import HttpResponse 
from appTercerPreEntrega.models import *
from appTercerPreEntrega.forms import *

# Create your views here.

def usuario(request):

    return render(request, "appHtml/usuario.html")

def propiedades(request):

    return render(request, "appHtml/propiedades.html")

def inversores(request):

    return render(request, "appHtml/inversores.html")

def agregarUsuario(request):

    if request.method == "POST":

        form = usuarioFormulario(request.POST)

        if form.is_valid():

            informacion = form.cleaned_data

            usuario1 = usuario(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])

            usuario1.save()

            return render(request, "appHtml/formUsuario.html")
        
    else:
        form = usuarioFormulario()

    return render(request, "appHtml/formUsuario.html", {"formularioUsuario" : form})


def buscarUsuario(request):

     return render(request, "appHtml/busquedaUsuario.html")

def resultadoBusqueda(request):

    if request.GET["Usuario"]:

        Usuario = reuqest.GET["Usuario"]
        nombre = usuario.objects.filter(Usuario__iexacts=Usuario)

        return render(request, "appHtml/resultados.html", {'nombre':nombre, "Usuario": Usuario})

    else:

        respuesta = "No enviaste datos."




    return HttpResponse(respuesta)
