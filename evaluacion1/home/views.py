# home/views.py

from django.shortcuts import render
from django.template import TemplateDoesNotExist

def index(request):
    return render(request, 'index.html')  # Asegúrate de que 'index.html' esté en 'evaluacion1/templates/'

def Galeria(request):
    contenido = {
        'titulo': 'Página Secundaria',
        'descripcion': 'Esta es una página secundaria que incluye imágenes y enlaces.',
    }
    return render(request, 'Galeria.html', contenido)  # Debe estar en 'evaluacion1/templates/'

def contacto(request):
    return render(request, 'contacto.html')  # Debe estar en 'evaluacion1/templates/'


def test_template(request):
    try:
        return render(request, 'index.html')
    except TemplateDoesNotExist:
        return print("¡No se encontró la plantilla 'index.html'!")