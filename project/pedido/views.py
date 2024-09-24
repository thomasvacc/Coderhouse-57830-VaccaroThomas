from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import PedidoForm
from .models import Pedido

def index(request):
    return render(request, 'pedido/index.html')


class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pedido.objects.filter(nombre__icontains=q)
        return queryset

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoDetail(LoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'object'
    template_name = 'pedido/pedido_detail.html'

class PedidoUpdate(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido:pedido_list')