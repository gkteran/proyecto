from django.urls import path
from .views import index, agregar_datos, buscar

urlpatterns = [
    path('', index, name='index'),
    path('agregar/', agregar_datos, name='agregar_datos'),
    path('buscar/', buscar, name='buscar'),
]
