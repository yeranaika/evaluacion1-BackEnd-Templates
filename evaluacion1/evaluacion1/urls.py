# evaluacion1/urls.py
from django.contrib import admin
from django.urls import path
from home import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Galeria/', views.galeria, name='Galeria'),  # Cambia 'Galeria' a 'galeria'
    path('contacto/', views.contacto, name='contacto'),
    path('test/', views.test_template, name='test_template'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),  # Esta línea necesita que la función exista en views
    path('formulario-cotizacion/', views.formulario_cotizacion, name='formulario_cotizacion'),
    path('tatuaje/<int:id>/', views.detalle_tatuaje, name='detalle_tatuaje'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),  # Asegúrate de que esta línea esté presente
    path('clientes/', views.AdminUsuario, name='AdminUsuario.html'),
    path('tatuaje/agendar/<int:tatuaje_id>/', views.agendar_cita, name='agendar_cita'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)