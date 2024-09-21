from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.index, name='index'),
    path("detail/<int:pk>", views.pedido_detail, name= "pedido_detail"),
    path("create/", views.pedido_create, name= "pedido_create"),
    path("list/", views.pedido_list, name= "pedido_list"),
]