from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=100, blank=True)
    biografia_breve = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    class EstadoLectura(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        EN_PROGRESO = 'en_progreso', 'En progreso'
        LEIDO = 'leido', 'Leído'

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100, blank=True)
    estado_lectura = models.CharField(
        max_length=20,
        choices=EstadoLectura.choices,
        default=EstadoLectura.PENDIENTE,
    )
    fecha_adquisicion = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    # Control de concurrencia: bloqueo optimista
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo
