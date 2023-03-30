from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo_articulo = models.CharField(max_length = 100)
    autor = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name ="Autor")
    fecha_de_creacion = models.DateTimeField(auto_now_add = True)
    imagen_principal = models.ImageField(upload_to = "publicaciones", null = True, blank = True)
    breve_descripcion = models.CharField(max_length = 200)
    descripcion_articulo_inicio = models.CharField(max_length = 1000)
    imagen_1_de_nota = models.ImageField(upload_to = "publicaciones", null = True, blank = True)
    descripcion_articulo_desarrollo = models.CharField(max_length = 1000)
    imagen_2_de_nota = models.ImageField(upload_to = "publicaciones", null = True, blank = True)
    descripcion_articulo_conclusion = models.CharField(max_length = 1000)
    
    
    @property
    def imagen_principal_url(self):
        return self.imagen_principal.url if self.imagen_principal else ''
    

    @property
    def imagen_1_de_nota_url(self):
        return self.imagen_1_de_nota.url if self.imagen_1_de_nota else ''
    

    @property
    def imagen_2_de_nota_url(self):
        return self.imagen_2_de_nota.url if self.imagen_2_de_nota else ''
    

    def __str__(self):
        return f"{self.id} - {self.titulo_articulo}"