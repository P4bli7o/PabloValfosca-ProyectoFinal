"""Proyecto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Worldtech.views import (index, about_me, ArticuloList,  ArticuloDetail, ArticuloUpdate, 
                             ArticuloDelete, ArticuloCreate, ArticuloSearch, 
                             Login, SignUp, Logout, 
                             ArticulosMiosList, ProfileCreate, ProfileUpdate,
                             MensajeCreate, MensajeDelete, MensajeList, MensajeDetail)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('sobre-mi/', about_me, name = "sobre-mi"),
    path('lista/articulos/', ArticuloList.as_view(), name = "lista-articulos"),
    path('detalle/articulo/<pk>/', ArticuloDetail.as_view(), name = "detalle-articulo"),
    path('actualizar/articulo/<pk>/', ArticuloUpdate.as_view(), name = "actualizar-articulo"),
    path('eliminar/articulo/<pk>/', ArticuloDelete.as_view(), name = "eliminar-articulo"),
    path('crear/articulo/', ArticuloCreate.as_view(), name = "crear-articulo"),
    path('buscar/articulo/', ArticuloSearch.as_view(), name = "buscar-articulo"),
    path('iniciar-sesion/', Login.as_view(), name = "login"),
    path('registrarse/', SignUp.as_view(), name = "signup"),
    path('cerrar-sesion/', Logout.as_view(), name = "logout"),
    path('lista/articulos/mios', ArticulosMiosList.as_view(), name = "mis-articulos"),    
    path('crear-perfil/', ProfileCreate.as_view(), name = "crear-perfil"),
    path('actualizar-perfil/<pk>/', ProfileUpdate.as_view(), name = "actualizar-perfil"),
    path('lista/mensajes/', MensajeList.as_view(), name="lista-mensajes" ),
    path('crear/mensaje/', MensajeCreate.as_view(), name="crear-mensaje" ),
    path('eliminar/mensaje/<pk>/', MensajeDelete.as_view(), name="eliminar-mensaje"),
    path('detalle/mensaje/<pk>/', MensajeDetail.as_view(), name = "detalle-mensaje"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)