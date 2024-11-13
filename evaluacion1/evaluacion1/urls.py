# evaluacion1/urls.py
from django.contrib import admin
from django.urls import path
from home import views  # Asegúrate de importar desde el módulo correcto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Galeria/', views.Galeria, name='Galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('test/', views.test_template, name='test_template'),
    path('tatuajes/', views.lista_tatuajes, name='lista_tatuajes'),  # Esta línea necesita que la función exista en views
    path('carrito/', views.ver_carrito, name='ver_carrito'),  # Asegúrate de que esta línea esté presente
]
