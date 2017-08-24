from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Categoria, Pergunta


@login_required()
def get_pergunta(request):
    if request.method == 'POST':
        nova_pergunta = request.POST.get("pergunta")
        nova_resposta = request.POST.get("resposta")
        nova_alternativa = request.POST.get("alternativa")
        nova_categoria = Categoria.objects.get(
                         pk=request.POST.get("categoria"))
        usuario = request.user

        p = Pergunta(descricao=nova_pergunta,
                     resposta=nova_resposta,
                     alternativa=nova_alternativa,
                     categoria=nova_categoria,
                     criador=usuario)
        p.save()

        return HttpResponseRedirect('/pergunta/')

    categorias = Categoria.objects.all()
    return render(request, 'pergunta.html', {'categorias': categorias})


@login_required()
def nova_categoria(request):
    if request.method == 'POST':
        nome_cat = request.POST.get("cat")
        usuario = request.user
        print(nome_cat)
        lista = [x.nome for x in Categoria.objects.all()]
        if nome_cat not in lista and nome_cat is not None:
            cat = Categoria(nome=nome_cat,
                            criador=usuario)
            cat.save()
            return HttpResponseRedirect('/pergunta/')

    return render(request, 'categoria.html')


@login_required()
def perfil(request):
    perguntas = Pergunta.objects.filter(criador=request.user)

    return render(request, 'perfil.html', {'perguntas': perguntas})


def index(request):
    return render(request, 'index.html')
