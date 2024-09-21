from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente

@login_required
def index(request):
    return render(request, 'cliente/index.html')

def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, 'cliente/cliente_list.html', context)


def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:cliente_list')

    return render(request, 'cliente/cliente_create.html', {'form': form})

def cliente_detail(request, id):
    query = Cliente.objects.get(pk=id)
    context = {'object': query}
    return render(request, 'cliente/cliente_detail.html', context)
