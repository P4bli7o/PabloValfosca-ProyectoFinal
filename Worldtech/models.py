from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo_articulo = models.CharField(max_length=50)
    #autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autor")
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    #imagen_principal=  models.ImageField(upload_to="posts", null=True, blank=True)
    breve_descripcion = models.CharField(max_length=100)
    descripcion_articulo_inicio = models.CharField(max_length=500)
    #imagen_de_nota_1 = models.ImageField(upload_to="posts", null=True, blank=True)
    descripcion_articulo_desarrollo = models.CharField(max_length=500)
    #imagen_de_nota_2 = models.ImageField(upload_to="posts", null=True, blank=True)
    descripcion_articulo_conclusion = models.CharField(max_length=500)
    

    def __str__(self):
        return f"{self.id} - {self.titulo_articulo}"