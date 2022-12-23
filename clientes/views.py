from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from .forms import ClienteForma
# Create your views here.

def print_in_screen(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        print('Entro condicional')
        formulario.save()
        return redirect('clientes')
    print('No Entro condicional')
    return render(request, 'registro_clientes.html', {'formulario':formulario})
    
def print_message(request):
    return render(request, 'advertencia.html')

def view_clients(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes':clientes})

def mostrar_form(request):
    form = ClienteForma()
    if request.method == "POST":
        #print(request.POST)
        form = ClienteForma(request.POST)
        if form.is_valid():
            print("valido")
            cliente = Cliente()
            cliente.nombres = form.cleaned_data['nombres']
            cliente.apellido_paterno = form.cleaned_data['apellido_paterno']
            cliente.apellido_materno = form.cleaned_data['apellido_materno']
            cliente.fecha_alta = form.cleaned_data['fecha_alta']
            cliente.fecha_actualizacion = form.cleaned_data['fecha_actualizacion']
            cliente.num_cliente = form.cleaned_data['num_cliente']

            cliente.save()
        else:
            print("invalido")
    return render(request, 'agregar_cliente.html', {'form' : form})



   