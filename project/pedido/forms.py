from django import forms
from .models import Pedido
from panaderia.models import Panaderia
from cliente.models import Cliente

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), empty_label="Seleccione un cliente"
    )
    servicio = forms.ModelChoiceField(
        queryset=Panaderia.objects.filter(disponible=True), empty_label="Seleccione un servicio"
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {"fecha_entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})}