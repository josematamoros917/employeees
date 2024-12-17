from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/sign_up.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': f"Usuario '{user.username}' creado exitosamente con rol '{user.perfil.rol}'."
            }, status=200)

        messages.success(self.request, f"Usuario '{user.username}' creado exitosamente con rol '{user.perfil.rol}'.")
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'error',
                'message': 'El formulario contiene errores.',
                'errors': form.errors.as_json()
            }, status=400)
        return super().form_invalid(form)
