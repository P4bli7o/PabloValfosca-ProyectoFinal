from django.shortcuts import render
from Worldtech.models import Articulo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request, "Worldtech/index.html")


class ArticuloList(ListView):
    model = Articulo
    context_object_name = "articulos"

class ArticuloDetail(DetailView):
    model = Articulo
    context_object_name = "articulo"

class ArticuloUpdate(UpdateView):
    model = Articulo
    success_url = reverse_lazy("lista-articulo")
    fields = '__all__'
    
class ArticuloDelete(DeleteView):
    model = Articulo
    context_object_name = "articulo"
    success_url = reverse_lazy("lista-articulo")

class ArticuloCreate(CreateView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "Worldtech/crear_form.html"
    success_url = reverse_lazy("lista-articulo")
    fields = '__all__'
    




   
class ArticuloSearch(ListView):
    model = Articulo
    context_object_name = "articulos"
    template_name = "Worldtech/buscar.html"
    

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        if criterio != "" and criterio != " ":
            resultado = Articulo.objects.filter(titulo_articulo__icontains = criterio).all()
            return resultado
        else:
            resultado = []
            return resultado

