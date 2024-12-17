from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    TrabajadorListView,
    TrabajadorCreateView,
    TrabajadorDeleteView,
    TrabajadorUpdateView,
    HomeView
)
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('list/', TrabajadorListView.as_view(), name='list'),
    path('create/', TrabajadorCreateView.as_view(), name='create'),
    path('update/<str:pk>/', TrabajadorUpdateView.as_view(), name='update'),  # Cambié <int:pk> a <str:pk>
    path('delete/<str:pk>/', TrabajadorDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
