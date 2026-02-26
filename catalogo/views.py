from django.shortcuts import render
from .models import Categoria, Mueble

def catalogo_view(request):
    # 1. Obtener el ID de categoría de la URL (si existe)
    categoria_id = request.GET.get('categoria')

    # 2. Obtener todas las categorías para los botones del filtro
    categorias = Categoria.objects.all()

    # 3. Filtrar muebles o traer todos
    if categoria_id:
        muebles = Mueble.objects.filter(categoria_id=categoria_id)
    else:
        muebles = Mueble.objects.all()

    return render(request, 'catalogo.html', {
        'muebles': muebles,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    })