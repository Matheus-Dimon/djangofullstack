from django.shortcuts import render
from .models import cadastro

def home(request):
    return render(request, 'templates/home.html')

def produtos_cadastrados(request):
    return render(request, 'templates/cadastro.html')

def trocas(request):
    return render(request, 'templates/trocas.html')

def lista_cadastro(request):
    return render(request, 'templates/produtos.html')

def newcad(request):
    novo_cadastro = cadastro()
    novo_cadastro.descrição = request.POST.get('descrição')
    novo_cadastro.marca = request.POST.get('marca')
    novo_cadastro.modelo = request.POST.get('modelo')
    novo_cadastro.preço = request.POST.get('preço')
    novo_cadastro.preço = request.POST.get('tipo')
    novo_cadastro.save()
    newcad = {
        'newcad' : cadastro.objects.all()
    }
    return render (request,'templates/cadastro.html',newcad)