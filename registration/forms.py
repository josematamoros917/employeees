from django import forms
from django.contrib.auth.models import User
from listaempleados.models import Trabajador
from .models import PerfilUsuario

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar Contraseña'}),
    )
    rol = forms.ChoiceField(
        label="Rol",
        choices=PerfilUsuario.ROLES,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
    )
    rut = forms.CharField(
        label="RUT",
        max_length=9,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'RUT'}),
    )
    first_name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}),
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Apellido'}),
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Correo Electrónico'}),
    )
    cargo = forms.CharField(
        label="Cargo",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Cargo'}),
    )
    sexo = forms.ChoiceField(
        label="Sexo",
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
    )
    direccion = forms.CharField(
        label="Dirección",
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Dirección'}),
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Teléfono'}),
    )
    image = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file mb-3'}),
    )
    fecha_ingreso = forms.DateField(
        label="Fecha de Ingreso",
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Fecha de Ingreso',
                'type': 'date'
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'rut', 'cargo', 'sexo', 'direccion', 'telefono', 'image', 'fecha_ingreso', 'rol')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

            # Crear perfil de usuario y trabajador
            PerfilUsuario.objects.create(user=user, rol=self.cleaned_data.get("rol"))
            Trabajador.objects.create(
                user=user,
                nombre=self.cleaned_data.get("first_name"),
                apellido=self.cleaned_data.get("last_name"),
                rut=self.cleaned_data.get("rut"),
                cargo=self.cleaned_data.get("cargo"),
                sexo=self.cleaned_data.get("sexo"),
                correo=user.email,
                direccion=self.cleaned_data.get("direccion"),
                telefono=self.cleaned_data.get("telefono"),
                perfil_editado=False,
                image=self.cleaned_data.get("image"),
                fecha_ingreso=self.cleaned_data.get("fecha_ingreso")
            )
        return user
