# home/views.py

from django.shortcuts import render
from django.template import TemplateDoesNotExist

def index(request):
    return render(request, 'index.html')  # Asegúrate de que 'index.html' esté en 'evaluacion1/templates/'

def Galeria(request):
    contenido1 = {
        'titulo': 'Galeria',
        'descripcion': '//////// Tatuajes realizados :P ////////',
    }
    return render(request, 'Galeria.html', contenido1)  # Debe estar en 'evaluacion1/templates/'
    

def contacto(request):
    return render(request, 'contacto.html')  # Debe estar en 'evaluacion1/templates/'


def test_template(request):
    try:
        return render(request, 'index.html')
    except TemplateDoesNotExist:
        return print("¡No se encontró la plantilla 'index.html'!")