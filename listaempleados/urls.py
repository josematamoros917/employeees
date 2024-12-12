from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TrabajadorListView , TrabajadorCreateView, TrabajadorDeleteView, TrabajadorUpdateView

urlpatterns = [
    path('', TrabajadorListView.as_view(), name='list'),
    path('create/', TrabajadorCreateView.as_view(), name='create'),
    path('delete/<int:pk>', TrabajadorDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', TrabajadorUpdateView.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)