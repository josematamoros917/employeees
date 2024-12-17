from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Trabajador
from .forms import TrabajadorForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "listaempleados/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trabajador = get_object_or_404(Trabajador, user=self.request.user)
        context['trabajador'] = trabajador
        return context


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