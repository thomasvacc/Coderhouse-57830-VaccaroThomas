from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from .forms import ClienteForm
from .models import Cliente

def index(request):
    return render(request, 'cliente/index.html')

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff # type: ignore
    
    def handle_no_permission(self):
        return redirect('core:index')

class ClienteList(AdminRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Cliente.objects.filter(nombre__icontains=q)
        return queryset

class ClienteCreate(AdminRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteDetail(AdminRequiredMixin, DetailView):
    model = Cliente
    context_object_name = 'object'
    template_name = 'cliente/cliente_detail.html'

class ClienteUpdate(AdminRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteDelete(AdminRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente:cliente_list')

class PedidoIndex(AdminRequiredMixin, View):  # Cambiar a View
    def get(self, request):
        return render(request, 'cliente/index.html')