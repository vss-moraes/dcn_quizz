from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    resposta = models.CharField(max_length=100)
    alternativa = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return self.descricao


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class UsuarioResposta(models.Model):
    usuario = models.ForeignKey(Perfil)
    pergunta = models.ForeignKey(Pergunta)
    resposta = models.CharField(max_length=50)
    classificacao = models.IntegerField(default=0)

    def __str__(self):
        return str(self.classificacao)
