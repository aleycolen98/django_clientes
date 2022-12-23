from django import forms
from .models import Cliente
from .models import CuentaCliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteForma(forms.Form):

    nombres = forms.CharField(label="Nombre(s)", max_length=100)
    apellido_paterno = forms.CharField(label="Apellido Paterno", max_length=100)
    apellido_materno = forms.CharField(label="Apellido Materno", max_length=100)
    fecha_alta = forms.DateField(label="Fecha alta", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_actualizacion = forms.DateField(label="Fecha actualizacion", widget=forms.DateInput(attrs={'type': 'date'}))
    num_cliente = forms.IntegerField(label="Numero del cliente")

class CuentaForma(forms.Form):
    
    cliente = forms.ModelChoiceField(label="Cliente", queryset=Cliente.values_list('id', flat=True))
    num_cuenta = forms.IntegerField(label="Numero de cuenta")
    Tipo_cuenta = forms.CharField(label="Tipo de cuenta")

