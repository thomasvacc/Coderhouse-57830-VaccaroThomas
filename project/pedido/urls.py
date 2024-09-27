from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.PedidoIndex.as_view(), name='index'),
    path('list/', views.PedidoList.as_view(), name='pedido_list'),
    path('create/', views.PedidoCreate.as_view(), name='pedido_create'),
    path('detail/<int:pk>/', views.PedidoDetail.as_view(), name='pedido_detail'),
    path('update/<int:pk>/', views.PedidoUpdate.as_view(), name='pedido_update'),
    path('delete/<int:pk>/', views.PedidoDelete.as_view(), name='pedido_delete'),
]