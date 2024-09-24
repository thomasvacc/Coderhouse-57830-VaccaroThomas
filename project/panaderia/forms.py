from django import forms
from .models import Panaderia

class PanaderiaForm(forms.ModelForm):
    class Meta:
        model = Panaderia
        fields = "__all__"
   
