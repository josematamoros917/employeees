from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trabajador
from .forms import TrabajadorForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class TrabajadorListView(ListView):
    model = Trabajador
    template_name =  'listaempleados/list_view.html'
    context_object_name = 'trabajadores'

@method_decorator(login_required, name='dispatch')
class TrabajadorCreateView(CreateView):
    model = Trabajador
    template_name = 'listaempleados/create_view.html'
    success_url = reverse_lazy('list')
    form_class = TrabajadorForm

@method_decorator(login_required, name='dispatch')
class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'listaempleados/delete_view.html'
    success_url = reverse_lazy('list')

@method_decorator(login_required, name='dispatch')
class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    template_name = 'listaempleados/update_view.html'
    success_url = reverse_lazy('list')
    form_class = TrabajadorForm