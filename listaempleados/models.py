from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=9, primary_key=True)
    cargo = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    image = models.ImageField(upload_to='trabajadores')
    
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil_editado = models.BooleanField(null=True, default=False) # para detectar si el perfil fue editado

    
    fecha_ingreso = models.DateField(null=True, blank=True)  # Campo opcional inicialmente

    def set_fecha_ingreso_si_no_existe(self):
        if not self.fecha_ingreso:
            self.fecha_ingreso = timezone.now()
            self.save()
    def __str__(self):
        return self.nombre