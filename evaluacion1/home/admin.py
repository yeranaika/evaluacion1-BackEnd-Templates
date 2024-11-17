# En tu archivo admin.py
from django.contrib import admin
from .models import Cliente, Tatuaje, Cita, ImagenTatuaje ,Carrito , Producto

admin.site.register(Cliente)
admin.site.register(Tatuaje)
admin.site.register(ImagenTatuaje)
admin.site.register(Cita)
admin.site.register(Carrito)
admin.site.register(Producto)