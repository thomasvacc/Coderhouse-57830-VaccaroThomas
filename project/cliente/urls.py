from django.urls import path

from . import views

app_name = 'cliente'


urlpatterns = [
    path('', views.PedidoIndex.as_view(), name='index'),
    path('list', views.ClienteList.as_view(), name='cliente_list'),
    path('form', views.ClienteCreate.as_view(), name='cliente_form'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='cliente_detail'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='cliente_delete'),
]