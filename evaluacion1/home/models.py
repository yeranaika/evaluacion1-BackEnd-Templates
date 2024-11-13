from django.db import models
from django.contrib.auth.models import User  # Asumiendo que utilizas el modelo de usuario de Django

# Modelo de Cliente
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.usuario.username

# Modelo de Tatuaje
class Tatuaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    medida = models.DecimalField(max_digits=5, decimal_places=2)  # Por ejemplo, en centímetros
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio asociado a la medida

    def __str__(self):
        return f"{self.nombre} - {self.medida} cm"

# Modelo de Cita
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tatuaje = models.ForeignKey(Tatuaje, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('completada', 'Completada'), ('cancelada', 'Cancelada')], default='pendiente')

    def __str__(self):
        return f"Cita de {self.cliente.usuario.username} para {self.tatuaje.nombre} el {self.fecha}"

# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo de Carrito
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - {self.usuario.username}"