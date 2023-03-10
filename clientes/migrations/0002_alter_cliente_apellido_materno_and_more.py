# Generated by Django 4.1.4 on 2022-12-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido_materno',
            field=models.CharField(max_length=100, verbose_name='apellido_mat'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_paterno',
            field=models.CharField(max_length=100, verbose_name='apellido_pat'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_actualizacion',
            field=models.DateField(verbose_name='fecha_actualizacion'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(verbose_name='fecha_registro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(max_length=100, verbose_name='nombres'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_cliente',
            field=models.IntegerField(verbose_name='numero_cliente'),
        ),
    ]
