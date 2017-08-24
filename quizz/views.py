from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Categoria, Pergunta


def get_pergunta(request):
    if request.method == 'POST':
        nova_pergunta = request.POST.get("pergunta")
        nova_resposta = request.POST.get("resposta")
        nova_alternativa = request.POST.get("alternativa")
        nova_categoria = Categoria.objects.get(
                         pk=request.POST.get("categoria"))

        p = Pergunta(descricao=nova_pergunta,
                     resposta=nova_resposta,
                     alternativa=nova_alternativa,
                     categoria=nova_categoria)
        p.save()

        return HttpResponseRedirect('/pergunta/')

    categorias = Categoria.objects.all()
    return render(request, 'pergunta.html', {'categorias': categorias})


def nova_categoria(request):
    if request.method == 'POST':
        nome_cat = request.POST.get("cat")
        print(nome_cat)
        lista = [x.nome for x in Categoria.objects.all()]
        if nome_cat not in lista and nome_cat is not None:
            cat = Categoria(nome=nome_cat)
            cat.save()
            return HttpResponseRedirect('/pergunta/')

    return render(request, 'categoria.html')


def novo_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        nome_usuario = request.POST.get("username")
        e_mail = request.POST.get("email")
        senha = request.POST.get("senha")
        print(nome_usuario)
        usuario = User.objects.create_user(username=nome_usuario,
                                           email=e_mail,
                                           password=senha,
                                           first_name=nome,
                                           last_name=sobrenome)
        usuario.save()
        return HttpResponseRedirect(reverse('pagina_inicial'))
    return render(request, 'registration/novo_usuario.html')


def index(request):
    return render(request, 'index.html')
