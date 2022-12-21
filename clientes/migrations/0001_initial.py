# Generated by Django 4.1.4 on 2022-12-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField()),
                ('fecha_actualizacion', models.DateField()),
                ('num_cliente', models.IntegerField()),
            ],
        ),
    ]
