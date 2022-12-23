from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Cliente(models.Model):
    
    id =  models.AutoField(primary_key=True)
    nombres = models.CharField(max_length = 100, verbose_name='nombres')
    apellido_paterno = models.CharField(max_length = 100, verbose_name='apellido_pat')
    apellido_materno = models.CharField(max_length = 100, verbose_name='apellido_mat')
    fecha_alta = models.DateField(verbose_name='fecha_registro')
    fecha_actualizacion = models.DateField(verbose_name='fecha_actualizacion')
    num_cliente = models.IntegerField(verbose_name='numero_cliente')

#Clase de la cuenta, contendra la relacion con el cliente
class CuentaCliente(models.Model):

    class TipoCuenta(models.TextChoices):
        REF = 0, _('Referencia')
        CT = 1, _('CT')
        PAG = 2, _('PAGARE')

    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_cuenta = models.IntegerField(verbose_name="numero_cuenta")
    tipo_de_cuenta = models.TextField(default=TipoCuenta.REF, choices=TipoCuenta.choices)