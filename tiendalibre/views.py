from django.shortcuts import render
from .models import Producto



def productos(request):
    lista_productos = Producto.objects.filter(activo=True)
    return render(request, 'tiendalibre/productos.html', {'productos': lista_productos})

def home(request):
    return render(request, "tiendalibre/home.html")


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")