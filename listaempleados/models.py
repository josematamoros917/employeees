from django.db import models
from django.contrib.auth.models import User

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=9, primary_key=True)
    cargo = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    image = models.ImageField(upload_to='trabajadores')
    fecha_ingreso = models.DateField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre