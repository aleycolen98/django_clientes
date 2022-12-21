from django.db import models

# Create your models here.

class Cliente(models.Model):
    id =  models.AutoField(primary_key=True)
    nombres = models.CharField(max_length = 100, verbose_name='nombres')
    apellido_paterno = models.CharField(max_length = 100, verbose_name='apellido_pat')
    apellido_materno = models.CharField(max_length = 100, verbose_name='apellido_mat')
    fecha_alta = models.DateField(verbose_name='fecha_registro')
    fecha_actualizacion = models.DateField(verbose_name='fecha_actualizacion')
    num_cliente = models.IntegerField(verbose_name='numero_cliente')

    