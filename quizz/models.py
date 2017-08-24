from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    criador = models.ForeignKey(User)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    resposta = models.CharField(max_length=100)
    alternativa = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categoria)
    criador = models.ForeignKey(User)

    def __str__(self):
        return self.descricao


class UsuarioResposta(models.Model):
    usuario = models.ForeignKey(User)
    pergunta = models.ForeignKey(Pergunta)
    resposta = models.CharField(max_length=50)
    classificacao = models.IntegerField(default=0)

    def __str__(self):
        return str(self.classificacao)
