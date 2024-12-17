"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta hacia listaempleados
    path('', include('listaempleados.urls')),
    
    # Rutas relacionadas con el sistema de autenticación
    path('accounts/', include('registration.urls')),  # Primero las rutas de registro personalizadas
    path('accounts/', include('django.contrib.auth.urls')),  # Luego las rutas predeterminadas de Django

    # Redirige de `accounts/profile/` a la página de inicio
    path('accounts/profile/', RedirectView.as_view(url='/')),

    # Ruta al panel de administrador
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
