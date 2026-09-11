from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad")
    search_fields = ("nombre",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "estado_lectura", "fecha_adquisicion")
    list_filter = ("estado_lectura", "genero")
    search_fields = ("titulo", "autor__nombre")
