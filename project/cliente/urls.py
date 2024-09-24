from django.urls import path

from . import views

app_name = 'cliente'


urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/list', views.ClienteList.as_view(), name='cliente_list'),
    path('cliente/form', views.ClienteCreate.as_view(), name='cliente_form'),
    path('cliente/detail/<int:pk>/', views.ClienteDetail.as_view(), name='cliente_detail'),
    path('cliente/update/<int:pk>/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', views.ClienteDelete.as_view(), name='cliente_delete'),
]