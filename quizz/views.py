from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

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

@login_required()
def mudar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('change_password')
        else:
            messages.error(request, 'Algo deu errado.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/mudar_senha.html', {
        'form': form
    })

def index(request):
    return render(request, 'index.html')
