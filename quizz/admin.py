from django.contrib import admin
from .models import Categoria, Pergunta, UsuarioResposta

admin.site.register(Categoria)
admin.site.register(UsuarioResposta)
admin.site.register(Pergunta)
