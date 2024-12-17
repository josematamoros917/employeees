from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PerfilUsuario(models.Model):
    ROLES = (
        ('Admin', 'Administrador'),
        ('Trabajador-RRHH', 'Empleado-RRHH'),
        ('Trabajador', 'Trabajador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='Trabajador')

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
