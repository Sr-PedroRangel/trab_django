from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def home(request):
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        saudacao = "Bom dia!"
    else:
        saudacao = "Boa tarde!"

    contexto = {
        "mensagem": f"{saudacao}! São {datetime.now().strftime("%H:%M")}. Servidor ligado e respondendo.",
        "nome_aluno": "Pedro Rangel Machado",
    }

    return render(request, 'pages/home.html', contexto)


def contato(request):

    return render(request, 'pages/contato.html')


def sobre(request):
    return render(request, 'pages/sobre.html')


def ajuda(request):
    return render(request, 'pages/ajuda.html')