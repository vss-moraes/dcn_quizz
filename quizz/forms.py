from django import forms

from .models import Categoria


class PerguntaForm(forms.Form):
    pergunta = forms.SlugField(label="Pergunta")
    resposta = forms.CharField(label="Resposta", max_length=100)
    alternativa = forms.CharField(label="Resposta Alternativa", max_length=100)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())


class CategoriaForm(forms.Form):
    nome = forms.CharField(label="Categoria", max_length=100)
