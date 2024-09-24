from django.contrib.auth.mixins import LoginRequiredMixin
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
            queryset = Panaderia.objects.filter(nombre__icontains=q)
        return queryset

class PanaderiaCreate(LoginRequiredMixin, CreateView):
    model = Panaderia
    form_class = PanaderiaForm
    success_url = reverse_lazy('panaderia:panaderia_list')

class PanaderiaDetail(LoginRequiredMixin, DetailView):
    model = Panaderia
    context_object_name = 'object'
    template_name = 'panaderia/panaderia_detail.html'

class PanaderiaUpdate(LoginRequiredMixin, UpdateView):
    model = Panaderia
    form_class = PanaderiaForm
    success_url = reverse_lazy('panaderia:panaderia_list')

class PanaderiaDelete(LoginRequiredMixin, DeleteView):
    model = Panaderia
    success_url = reverse_lazy('panaderia:panaderia_list')