from django.shortcuts import render
from .models import Producto
from django.views.generic import TemplateView
# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos}  )