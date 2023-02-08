from django.urls import path
from appTercerPreEntrega.views import *

urlpatterns = [
    path("verUsuarios/", usuario),
    path("verPropiedades/", propiedades),
    path("verInversores/", inversores),
    path("nuevoUsuario/", agregarUsuario),
    path("buscar/", buscarUsuario),
    path("resultados", resultadoBusqueda),
]
