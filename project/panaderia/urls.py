from django.contrib import admin
from django.urls import path
from . import views

app_name = 'panaderia'

urlpatterns = [
    path('', views.index, name='index'),
    path("panaderia/detail/<int:pk>", views.panaderia_detail, name= "panaderia_detail"),
    path("panaderia/create/", views.panaderia_create, name= "panaderia_create"),
    path("panaderia/list/", views.panaderia_list, name= "panaderia_list"),
]