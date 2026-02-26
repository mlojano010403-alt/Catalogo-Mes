from django.urls import path
from . import views

urlpatterns = [
    # Esta es la ruta para ver el catálogo
    path('', views.catalogo_view, name='catalogo'),
]