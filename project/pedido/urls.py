from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.index, name='index'),
    path("detail/<int:pk>", views.PedidoDetail.as_view(), name= "pedido_detail"),
    path("form/", views.PedidoCreate.as_view(), name= "pedido_form"),
    path("list/", views.PedidoList.as_view(), name= "pedido_list"),
    path('pedido/update/<int:pk>', views.PedidoUpdate.as_view(), name='pedido_update'),
    path('pedido/delete/<int:pk>', views.PedidoDelete.as_view(), name='pedido_delete'),
]