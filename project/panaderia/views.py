from django.shortcuts import render, redirect
from .models import Panaderia
from .forms import PanaderiaForm

def index(request):
    return render(request, "panaderia/index.html")

def panaderia_list(request):
    query = Panaderia.objects.all()
    context = {"object_list": query}
    return render(request, "panaderia/panaderia_list.html", context)


def panaderia_create(request):
    if request.method == "GET":
        form = PanaderiaForm()
    if request.method == "POST":
        form = PanaderiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("panaderia_list")
    return render(request, "panaderia/panaderia_create.html", {"form": form})


def panaderia_detail(request, pk: int):
    query = Panaderia.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'panaderia/panaderia_detail.html', context)
