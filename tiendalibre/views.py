from django.shortcuts import render
from .models import Producto


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def home(request):
    return render(request, "tiendalibre/home.html")


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")