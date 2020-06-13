from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


from django.shortcuts import render, redirect
from .models.fornecedores import t_fornecedor
from .models.clientes import t_cliente
from .models.eventos import t_evento
from .forms.forms import fornecedorForm, clienteForm, eventoForm


SCOPES = ['https://www.googleapis.com/auth/calendar']



def calendario(request):
    calendario = t_evento.objects.all()
    service = buildService()
    eventos = listarEventos(service)
    return render(request, 'calendario/calendario.html',{'calendario':calendario,'eventos': eventos })

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


##### INICIO DA API ##############33

def buildService():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('ALMSolutions/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def listarEventos(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        return 'Não existem proximos eventos.'
    return events


def criarEvento(service, assunto, local, descricao, dataInicio, dataFim):
    event = {
        'summary': assunto,
        'location': local,
        'description': descricao,
        'start': {
            'dateTime': dataInicio,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': dataFim,
            'timeZone': 'America/Sao_Paulo',
        },
        'attendees' : [
            {'email': 'alexjones19961996@gmail.com'},
        ]
    }

    event = service.events().insert(calendarId='alex.silva@aluno.faculdadeimpacta.com.br', body=event).execute()
    return 'Evento criado com sucesso'
