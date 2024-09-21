from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'cliente'


urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/list', login_required(views.cliente_list), name='cliente_list'),
    path('cliente/create', login_required(views.cliente_create), name='cliente_create'),
    path('cliente/detail/<int:id>/', login_required(views.cliente_detail), name='cliente_detail'),
]