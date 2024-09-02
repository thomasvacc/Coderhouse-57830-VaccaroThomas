from django.shortcuts import render, redirect
from .models import Cliente, Panaderia, Pedido
from .forms import ClienteForm, PanaderiaForm, PedidoForm

def index(request):
    return render(request, "panaderia/index.html")

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, "panaderia/cliente_list.html", context)

def panaderia_list(request):
    query = Panaderia.objects.all()
    context = {"object_list": query}
    return render(request, "panaderia/panaderia_list.html", context)

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, "panaderia/pedido_list.html", context)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "panaderia/cliente_create.html", {"form": form})

def panaderia_create(request):
    if request.method == "GET":
        form = PanaderiaForm()
    if request.method == "POST":
        form = PanaderiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("panaderia_list")
    return render(request, "panaderia/panaderia_create.html", {"form": form})


def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "panaderia/pedido_create.html", {"form": form})
