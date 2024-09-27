from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View
from .forms import PedidoForm
from .models import Pedido

def index(request):
    return render(request, 'pedido/index.html')

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff # type: ignore

    def handle_no_permission(self):
        return redirect('core:index')  # Redirige al inicio si no tiene permiso

class PedidoList(AdminRequiredMixin, ListView):
    model = Pedido

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pedido.objects.filter(nombre__icontains=q)
        return queryset

class PedidoCreate(AdminRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoDetail(AdminRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'object'
    template_name = 'pedido/pedido_detail.html'

class PedidoUpdate(AdminRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoDelete(AdminRequiredMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoIndex(AdminRequiredMixin, View): 
    def get(self, request):
        return render(request, 'pedido/index.html')