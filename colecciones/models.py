from django.db import models
from libros.models import Libro


class Coleccion(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    libros = models.ManyToManyField(Libro, related_name='colecciones', blank=True)

    def __str__(self):
        return self.nombre
