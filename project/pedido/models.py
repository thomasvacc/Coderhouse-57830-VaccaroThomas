from panaderia.models import Panaderia
from cliente.models import Cliente
from django.db import models

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO', 'En proceso'
        COMPLETADO = 'COMPLETADO', 'Completado'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio= models.ForeignKey(Panaderia, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Pedido de {self.servicio.nombre} para {self.cliente.nombre}"

