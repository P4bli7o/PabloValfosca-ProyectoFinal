from django.shortcuts import render
from Worldtech.models import Articulo, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from Worldtech.forms import UsuarioForm

def index(request):
    context = {
        "articulos": Articulo.objects.all().order_by("-fecha_de_creacion")[:6],
    }
    
    return render(request, "Worldtech/index.html", context)


def about_me(request): 
    return render(request, "Worldtech/sobre_mi.html")



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
    #form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('lista-articulos')


class Logout(LogoutView):
    template_name = 'registration/logout.html'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy('index')
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy('index')
    fields = ['avatar']

    def test_func(self):
        return Profile.objects.filter(user = self.request.user).exists()
    






class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('crear-mensaje')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy('lista-mensajes')

    def test_func(self):
        return Mensaje.objects.filter(destinatario = self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario = self.request.user).all()


class MensajeDetail(DetailView):
    model = Mensaje
    context_object_name = "mensaje"