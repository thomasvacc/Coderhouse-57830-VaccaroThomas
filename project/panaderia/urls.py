from django.contrib import admin
from django.urls import path
from . import views

app_name = 'panaderia'

urlpatterns = [
    path('', views.index, name='index'),
    path("panaderia/detail/<int:pk>", views.PanaderiaDetail.as_view(), name= "panaderia_detail"),
    path("panaderia/form/", views.PanaderiaCreate.as_view(), name= "panaderia_form"),
    path("panaderia/list/", views.PanaderiaList.as_view(), name= "panaderia_list"),
    path('panaderia/update/<int:pk>', views.PanaderiaUpdate.as_view(), name='panaderia_update'),
    path('panaderia/delete/<int:pk>', views.PanaderiaDelete.as_view(), name='panaderia_delete'),
]