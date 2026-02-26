from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        db_table = 'categorias'  # Obliga a Django a usar el nombre exacto de nuestra tabla SQL
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Mueble(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='muebles')
    nombre_mueble = models.CharField(max_length=150)
    archivo_imagen = models.CharField(max_length=255, unique=True)
    # Nueva línea:
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción Técnica")
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catalogo_muebles'

    def __str__(self):
        return self.nombre_mueble