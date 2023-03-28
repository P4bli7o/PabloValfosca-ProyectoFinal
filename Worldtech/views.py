from django.shortcuts import render
from Worldtech.models import Articulo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "Worldtech/index.html")


class ArticuloList(ListView):
    model = Articulo
    context_object_name = "articulos"

class ArticuloDetail(DetailView):
    model = Articulo
    context_object_name = "articulo"

class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy("lista-articulo")
    fields = '__all__'
    
class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    context_object_name = "articulo"
    success_url = reverse_lazy("lista-articulo")

class ArticuloCreate(LoginRequiredMixin, CreateView):
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






class Login(LoginView):
    next_page = reverse_lazy("index")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('lista-articulo')


class Logout(LogoutView):
    template_name = 'registration/logout.html'
