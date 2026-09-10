from django.db import models
from libros.models import Libro


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    fecha_resena = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.libro.titulo} ({self.calificacion}/5)"
