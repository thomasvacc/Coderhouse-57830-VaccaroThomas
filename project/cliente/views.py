from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import ClienteForm
from .models import Cliente

def index(request):
    return render(request, 'cliente/index.html')


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Cliente.objects.filter(nombre__icontains=q)
        return queryset

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('productos:cliente_list')

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    context_object_name = 'object'
    template_name = 'cliente/cliente_detail.html'

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente:cliente_list')