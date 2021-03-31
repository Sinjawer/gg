from django import forms
from .models import Cliente
from .models import Pedido

class  clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class  pedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
