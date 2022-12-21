from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

def print_in_screen(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        print('Entro condicional')
        formulario.save()
        return redirect('clientes')
    print('No Entro condicional')
    return render(request, 'registro_clientes.html', {'formulario':formulario})
    
5
def print_message(request):
    return render(request, 'advertencia.html')

def view_clients(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes':clientes})
    
   