from django.shortcuts import render
from django.template import TemplateDoesNotExist
from .models import Tatuaje  # Asegúrate de importar el modelo Tatuaje si es necesario

def index(request):
    return render(request, 'index.html')

def Galeria(request):
    contenido1 = {
        'titulo': 'Galeria',
        'descripcion': '//////// Tatuajes realizados :P ////////',
    }
    return render(request, 'Galeria.html', contenido1)

def contacto(request):
    return render(request, 'contacto.html')

def test_template(request):
    try:
        return render(request, 'index.html')
    except TemplateDoesNotExist:
        print("¡No se encontró la plantilla 'index.html'!")

def lista_tatuajes(request):
    tatuajes = Tatuaje.objects.all()  # Obtén todos los tatuajes desde el modelo
    return render(request, 'lista_tatuajes.html', {'tatuajes': tatuajes})


def ver_carrito(request):
    # Agrega la lógica de la vista o deja un placeholder por ahora
    return render(request, 'ver_carrito.html')  # Asegúrate de tener esta plantilla