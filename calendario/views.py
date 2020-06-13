from django.shortcuts import render, redirect
from .models.fornecedores import t_fornecedor
from .models.clientes import t_cliente
from .models.eventos import t_evento
from .forms.forms import fornecedorForm, clienteForm, eventoForm





def calendario(request):
    calendario = t_evento.objects.all()

    return render(request, 'calendario/calendario.html',{'calendario':calendario})

def cadastroevento(request):
    form = eventoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('calendario')

    return render(request, 'calendario/cadastroevento.html', {'form':form})


def atualizaevento(request, id):
    evento = t_evento.objects.get(id_evento=id)
    form = eventoForm(request.POST or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('calendario')

    return render(request, 'calendario/cadastroevento.html', {'form':form, 'evento': evento})


def apagarevento(request, id):
    evento = t_evento.objects.get(id_evento=id)

    if request.method == "POST":
        evento.delete()
        return redirect('calendario')

    return render(request, 'calendario/apagarevento.html', {'evento':evento})





def fornecedores(request):
    fornecedores = t_fornecedor.objects.all()
    return render(request, 'fornecedores/fornecedores.html', {'fornecedores':fornecedores})

def cadastrofornecedor(request):
    form = fornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('fornecedores')

    return render(request, 'fornecedores/cadastrofornecedores.html', {'form':form})


def atualizafornecedor(request, id):
    fornecedor = t_fornecedor.objects.get(id_fornecedor=id)
    form = fornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('fornecedores')

    return render(request, 'fornecedores/cadastrofornecedores.html', {'form':form, 'fornecedor': fornecedor})


def apagarfornecedor(request, id):
    fornecedor = t_fornecedor.objects.get(id_fornecedor=id)

    if request.method == "POST":
        fornecedor.delete()
        return redirect('fornecedores')

    return render(request, 'fornecedores/apagarfornecedor.html', {'fornecedor':fornecedor})



def clientes(request):
    clientes = t_cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes':clientes})

    
def cadastrocliente(request):
    form = clienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'clientes/cadastroclientes.html', {'form':form})


def atualizacliente(request, id):
    cliente = t_cliente.objects.get(id_cliente=id)
    form = clienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'clientes/cadastroclientes.html', {'form':form, 'cliente': cliente})


def apagarcliente(request, id):
    cliente = t_cliente.objects.get(id_cliente=id)

    if request.method == "POST":
        cliente.delete()
        return redirect('clientes')

    return render(request, 'clientes/apagarcliente.html', {'cliente':cliente})

