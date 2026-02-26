from django.contrib import admin
from .models import Categoria, Mueble

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre_mueble', 'categoria', 'fecha_agregado')
    list_filter = ('categoria',) # Te creará un filtro lateral súper útil
    search_fields = ('nombre_mueble', 'archivo_imagen')