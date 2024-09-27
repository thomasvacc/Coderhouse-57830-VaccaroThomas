from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import PanaderiaForm
from .models import Panaderia

def index(request):
    return render(request, 'panaderia/index.html')

class PanaderiaList(LoginRequiredMixin, ListView):
    model = Panaderia
    template_name = 'panaderia/panaderia_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff # type: ignore

    def handle_no_permission(self):
        return redirect('core:index')  # Redirige al inicio si no tiene permiso

class PanaderiaCreate(AdminRequiredMixin, CreateView):
    model = Panaderia
    form_class = PanaderiaForm
    success_url = reverse_lazy('panaderia:panaderia_list')

class PanaderiaDetail(LoginRequiredMixin, DetailView):
    model = Panaderia
    context_object_name = 'object'
    template_name = 'panaderia/panaderia_detail.html'

class PanaderiaUpdate(AdminRequiredMixin, UpdateView):
    model = Panaderia
    form_class = PanaderiaForm
    success_url = reverse_lazy('panaderia:panaderia_list')

class PanaderiaDelete(AdminRequiredMixin, DeleteView):
    model = Panaderia
    success_url = reverse_lazy('panaderia:panaderia_list')