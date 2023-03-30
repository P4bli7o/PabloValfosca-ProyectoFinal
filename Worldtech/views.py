from django.shortcuts import render
from Worldtech.models import Articulo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "Worldtech/index.html")


class ArticuloList(ListView):
    model = Articulo
    context_object_name = "articulos"

class ArticulosMiosList(LoginRequiredMixin, ArticuloList):
    queryset = Articulo.objects.all()

    def get_queryset(self):
        return Articulo.objects.filter(autor = self.request.user.id).all()



class ArticuloDetail(DetailView):
    model = Articulo
    context_object_name = "articulo"


# class AutorPermisos(UserPassesTestMixin):
#     def test_func(self):
#         id_usuario = self.request.user.id
#         id_articulo = self.kwargs.get("pk")
#         return Articulo.objects.filter(autor = id_usuario, id = id_articulo).exists()
    

class ArticuloUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy("lista-articulos")
    fields = '__all__'

    def test_func(self):
        id_usuario = self.request.user.id
        id_articulo = self.kwargs.get("pk")
        return Articulo.objects.filter(autor = id_usuario, id = id_articulo).exists()
    
    
class ArticuloDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    context_object_name = "articulo"
    success_url = reverse_lazy("lista-articulos")

    def test_func(self):
        id_usuario = self.request.user.id
        id_articulo = self.kwargs.get("pk")
        return Articulo.objects.filter(autor = id_usuario, id = id_articulo).exists()
    

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "Worldtech/crear_form.html"
    success_url = reverse_lazy("lista-articulos")
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
    success_url = reverse_lazy('lista-articulos')


class Logout(LogoutView):
    template_name = 'registration/logout.html'
