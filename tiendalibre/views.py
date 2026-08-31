from django.shortcuts import render
from .models import Producto



def productos(request):
    lista_productos = Producto.objects.filter(activo=True)
    return render(request, 'tiendalibre/productos.html', {'productos': lista_productos})

def home(request):

    lista_productos = [
        {
            'nombre': 'auriculares redragon',
            'marca': 'Redragon',
            'descripcion': 'Auriculares gamer con sonido envolvente, micrófono incorporado y gran comodidad para jugar.',
            'precio': 5.99,
            'stock': 10,
            'categoria': 'Periféricos',
            'imagen': None
        },
        {
            'nombre': 'teclado razer',
            'marca': 'Razer',
            'descripcion': 'Teclado mecánico gamer con iluminación RGB y teclas diseñadas para una respuesta rápida.',
            'precio': 49.99,
            'stock': 5,
            'categoria': 'Periféricos',
            'imagen': None
        },
        {
            'nombre': 'mouse logitech',
            'marca': 'Logitech',
            'descripcion': 'Mouse gamer ergonómico con sensor de alta precisión y botones programables.',
            'precio': 19.99,
            'stock': 8,
            'categoria': 'Periféricos',
            'imagen': None
        },
        {
            'nombre': 'monitor samsung',
            'marca': 'Samsung',
            'descripcion': 'Monitor Samsung de alta resolución, ideal para gaming, trabajo y entretenimiento.',
            'precio': 199.99,
            'stock': 3,
            'categoria': 'Monitores',
            'imagen': None
        },
        {
            'nombre': 'webcam logitech',
            'marca': 'Logitech',
            'descripcion': 'Webcam Full HD ideal para videollamadas, clases virtuales y transmisiones en vivo.',
            'precio': 39.99,
            'stock': 6,
            'categoria': 'Cámaras',
            'imagen': None
        },
        {
            'nombre': 'microfono gamer',
            'marca': 'Razer',
            'descripcion': 'Micrófono gamer de alta calidad para streaming, grabaciones y comunicación durante partidas.',
            'precio': None,
            'stock': 5,
            'categoria': 'Audio',
            'imagen': None
        },
    ]

    context = {

                'titulo': 'TIENDA LIBRE',
                'productos': lista_productos,
                'usuario_logueado': True,
            }

    return render(request, 'tiendalibre/home.html', context)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")