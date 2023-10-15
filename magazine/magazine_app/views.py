from django.shortcuts import render
from .models import cadastro


def index(request):
    return render(request, 'templates/index.html')

def lista_cadastro(request):
    return render(request, 'templates/produtos.html')

def newcad(request):
    novo_newcad = cadastro()
    novo_newcad.nome = request.POST.get('desc')
    novo_newcad.marca = request.POST.get('marc')
    novo_newcad.modelo = request.POST.get('mode')
    novo_newcad.preço = request.POST.get('prec')
    novo_newcad.save()
    cadastro = {
        'cadastro' : cadastro.objects.all()
    }
    return render (request,'templates/cadastro.html',cadastro)