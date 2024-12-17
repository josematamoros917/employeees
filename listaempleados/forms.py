from django import forms
from django.contrib.auth.models import User
from .models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'rut', 'sexo', 'correo', 'telefono', 'cargo', 'fecha_ingreso', 'direccion', 'image']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Excluir superusuarios de la lista de usuarios disponibles
            self.fields['user'].queryset = User.objects.filter(is_superuser=False)