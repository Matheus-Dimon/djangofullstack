from django.shortcuts import render
from .models import cadastro


def index(request):
    return render(request, 'templates/index.html')

def lista_cadastro(request):
    return render(request, 'templates/produtos.html')

def newcad(request):
    novo_cadastro = cadastro()
    novo_cadastro.nome = request.POST.get('desc')
    novo_cadastro.marca = request.POST.get('marc')
    novo_cadastro.modelo = request.POST.get('mode')
    novo_cadastro.preço = request.POST.get('prec')
    novo_cadastro.save()
    newcad = {
        'newcad' : cadastro.objects.all()
    }
    return render (request,'templates/cadastro.html',newcad)