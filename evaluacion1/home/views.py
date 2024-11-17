from django.shortcuts import render , redirect
from django.template import TemplateDoesNotExist
from .models import Tatuaje , CotizacionPersonalizada, TatuajePersonalizado, User, Cliente  # Asegúrate de importar el modelo Tatuaje si es necesario

from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

def galeria(request):
    tatuajes_disponibles = Tatuaje.objects.filter(realizado=False)  # Filtra los tatuajes disponibles
    tatuajes_realizados = Tatuaje.objects.filter(realizado=True)    # Filtra los tatuajes realizados
    return render(request, 'Galeria.html', {
        'tatuajes_disponibles': tatuajes_disponibles,
        'tatuajes_realizados': tatuajes_realizados
    })


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        comentario = request.POST.get('comentario')

        # Imprimir los datos para ver si se capturan correctamente
        print("Datos recibidos:")
        print(f"Nombre: {nombre}, Apellido: {apellido}, Correo: {correo}, Teléfono: {telefono}, Dirección: {direccion}, Comentario: {comentario}")

        # Verificar si el usuario ya existe
        if not User.objects.filter(username=correo).exists():
            # Crear un nuevo usuario con los campos necesarios
            user = User.objects.create(
                username=correo,
                email=correo,
                first_name=nombre,
                last_name=apellido
            )
            user.set_unusable_password()  # Opcional si no necesitas una contraseña

            # Crear el cliente asociado
            cliente = Cliente.objects.create(
                usuario=user,
                telefono=telefono,
                direccion=direccion
            )

            # Redirigir a una página de confirmación o mostrar un mensaje de éxito
            return redirect('index')  # Puedes cambiar 'index' por otra vista de confirmación si es necesario
        else:
            print("El usuario ya existe en la base de datos.")
    
    return render(request, 'contacto.html')

def test_template(request):
    try:
        return render(request, 'index.html')
    except TemplateDoesNotExist:
        print("¡No se encontró la plantilla 'index.html'!")

def cotizacion(request):
    tatuajes = Tatuaje.objects.all()  # Obtén todos los tatuajes desde el modelo
    tatuajes_personalizados = TatuajePersonalizado.objects.all()

    return render(request, 'cotizacion.html', 
                  {'tatuajes': tatuajes,
                   'tatuajes_personalizados': tatuajes_personalizados})

def detalle_tatuaje(request, id):
    tatuaje = get_object_or_404(Tatuaje, id=id)
    return render(request, 'detalle_tatuaje.html', {'tatuaje': tatuaje})

def ver_carrito(request):
    # Agrega la lógica de la vista o deja un placeholder por ahora
    return render(request, 'ver_carrito.html')  # Asegúrate de tener esta plantilla

def formulario_cotizacion(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre')
        tamano = request.POST.get('tamano')
        tipo = request.POST.get('tipo')
        observaciones = request.POST.get('observaciones')

        # Crear y guardar la cotización en la base de datos
        cotizacion = CotizacionPersonalizada(
            nombre_cliente=nombre_cliente,
            tamano=tamano,
            tipo=tipo,
            observaciones=observaciones
        )
        cotizacion.save()

        # Redirigir a una página de confirmación o mostrar un mensaje de éxito
        return redirect('confirmacion_cotizacion')  # Asegúrate de tener esta vista creada

    return render(request, 'formulario_cotizacion.html')

def AdminUsuario(request):
    clientes = Cliente.objects.all()
    return render(request, 'AdminUsuario.html', {'clientes': clientes})