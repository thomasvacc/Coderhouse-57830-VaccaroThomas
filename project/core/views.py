from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import PasswordChangeForm

from .forms import CustomUserCreationForm, UserProfileForm


def index(request):
    return render(request, 'core/index.html')


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def form_valid(self, form):
        messages.success(self.request, '¡Registro exitoso! Puedes iniciar sesión.')
        return super().form_valid(form)


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.get_form()
        context['password_form'] = PasswordChangeForm(user=self.request.user)  # type: ignore
        return context