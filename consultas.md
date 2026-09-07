Consultas ORM
1. Mostrar todos los productos
Producto.objects.all().values_list("nombre",)
2. Productos cuyo nombre contiene "a"
Producto.objects.filter(nombre__icontains="a").values_list("nombre",)
3. Productos con precio mayor a 1000
Producto.objects.filter(precio__gt=1000).values_list("nombre", )
4. Productos con precio menor a 5000
Producto.objects.filter(precio__lt=5000).values_list("nombre",)
5. Productos con stock mayor a 5
Producto.objects.filter(stock__gt=5).values_list("nombre",)
6. Productos activos
Producto.objects.filter(activo=True).values_list("nombre",)
7. Productos ordenados por precio de menor a mayor
Producto.objects.order_by("precio").values_list("nombre",)
8. Productos ordenados por precio de mayor a menor
Producto.objects.order_by("-precio").values_list("nombre",)
9. Productos con stock 1, 5 o 10
Producto.objects.filter(stock__in=[1, 5, 10]).values_list("nombre", )
10. Productos de la primera categoría
categoria = Categoria.objects.first()
categoria.productos.all().values_list("nombre",)