from django.shortcuts import render
from .forms import CategoriaForm, ProductoForm, ClienteForm, BusquedaForm

def index(request):
    return render(request, 'base.html')

def agregar_datos(request):
    return render(request, 'agregar_datos.html', {'categoria_form': CategoriaForm(),
                                                   'producto_form': ProductoForm(),
                                                   'cliente_form': ClienteForm()})

def buscar(request):
    return render(request, 'buscar.html', {'busqueda_form': BusquedaForm()})
