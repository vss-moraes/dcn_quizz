from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Categoria, Pergunta


def get_pergunta(request):
    if request.method == 'POST':
        nova_pergunta = request.POST.get("pergunta")
        nova_resposta = request.POST.get("resposta")
        nova_alternativa = request.POST.get("alternativa")
        nova_categoria = Categoria.objects.get(pk=request.POST.get("categoria"))

        p = Pergunta(descricao=nova_pergunta,
                     resposta=nova_resposta,
                     alternativa=nova_alternativa,
                     categoria=nova_categoria)
        p.save()

        return HttpResponseRedirect('/pergunta/')

    categorias = Categoria.objects.all()

    return render(request, 'pergunta.html', {'categorias': categorias})


def new_categoria(request):
    if request.method == 'POST':
        nome_cat = request.POST.get("cat")
        print(nome_cat)
        lista = [x.nome for x in Categoria.objects.all()]
        if nome_cat not in lista and nome_cat is not None:
            cat = Categoria(nome=nome_cat)
            cat.save()
            return HttpResponseRedirect('/pergunta/')

    return render(request, 'categoria.html')
