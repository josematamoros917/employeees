from django.contrib import admin
from django.contrib.auth.models import User
from .models import Trabajador
from registration.models import PerfilUsuario

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'apellido', 'rut', 'cargo', 'sexo', 'fecha_ingreso', 
        'correo', 'direccion', 'telefono', 'perfil_editado', 'mostrar_rol', 'user'
    )
    search_fields = ['nombre', 'apellido', 'rut', 'user__username', 'user__email']
    list_filter = ('sexo', 'cargo', 'user__perfil__rol')  # Filtrar por rol de PerfilUsuario
    readonly_fields = ('user',)  # Campo user será de solo lectura en la edición

    def mostrar_rol(self, obj):
        """
        Accede al rol desde el PerfilUsuario relacionado con el User del Trabajador.
        """
        return obj.user.perfil.rol if obj.user and hasattr(obj.user, 'perfil') else "Sin rol"

    mostrar_rol.short_description = 'Rol del Usuario'

    def save_model(self, request, obj, form, change):
        """
        Guarda el modelo y crea un User si aún no existe.
        """
        if not obj.user:  # Solo si no hay un usuario asociado
            user_data = form.cleaned_data
            
            # Buscar o crear el usuario
            user = User.objects.filter(email=user_data.get('correo')).first()
            if not user:
                user = User.objects.create_user(
                    username=user_data.get('username'),
                    email=user_data.get('correo'),
                    password=user_data.get('password1'),
                )
            obj.user = user
        
        obj.save()

# Registrar el modelo en el panel de administración
admin.site.register(Trabajador, TrabajadorAdmin)
