from django.shortcuts import render, redirect
from .forms import PedidoForm
from .models import Pedido

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, "pedido/pedido_list.html", context)

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    elif request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido:pedido_list') 
    return render(request, "pedido/pedido_create.html", {"form": form})

def pedido_detail(request, pk: int):
    query = Pedido.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'pedido/pedido_detail.html', context)

def index(request):
    return render(request, "pedido/index.html")