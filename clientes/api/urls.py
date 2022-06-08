from django import views
from django.urls import path
from clientes.api.views import ClientesView, ClientesDetalle

urlpatterns = [
    path('clientes-view/', ClientesView.as_view(), name='clientes-view'),
    path('clientes-detalle/<int:id>', ClientesDetalle.as_view(), name='clientes-detalle'),
]
