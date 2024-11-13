# En tu archivo admin.py
from django.contrib import admin
from .models import Cliente, Tatuaje, Cita

admin.site.register(Cliente)
admin.site.register(Tatuaje)
admin.site.register(Cita)
