from django.shortcuts import render, redirect
from .models.fornecedores import t_fornecedor
from .models.clientes import t_cliente
from .models.eventos import t_evento
from .forms.forms import fornecedorForm, clienteForm, eventoForm


def calendario(request):
    eventos = t_evento.objects.all()
    return render(request, 'calendario/calendario.html',{'eventos':eventos})

def cadastroevento(request):
    form = eventoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('calendario')

    return render(request, 'calendario/cadastroevento.html', {'form':form})



def fornecedores(request):
    fornecedores = t_fornecedor.objects.all()
    return render(request, 'calendario/fornecedores.html', {'fornecedores':fornecedores})

def cadastrofornecedores(request):
    form = fornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('fornecedores')

    return render(request, 'calendario/cadastrofornecedores.html', {'form':form})



def clientes(request):
    clientes = t_cliente.objects.all()
    return render(request, 'calendario/clientes.html', {'clientes':clientes})

    
def cadastrocliente(request):
    form = clienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'calendario/cadastroclientes.html', {'form':form})
