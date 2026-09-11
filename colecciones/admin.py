from django.contrib import admin
from .models import Coleccion


@admin.register(Coleccion)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    filter_horizontal = ("libros",)
