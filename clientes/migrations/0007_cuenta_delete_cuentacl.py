# Generated by Django 4.1.4 on 2022-12-23 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_cuentacl_delete_cuentac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_cuenta', models.IntegerField(verbose_name='numero_cuenta')),
                ('tipo_cuenta', models.TextField(choices=[('0', 'Referencia'), ('1', 'CT'), ('2', 'PAGARE')], default='0')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
        migrations.DeleteModel(
            name='CuentaCl',
        ),
    ]
