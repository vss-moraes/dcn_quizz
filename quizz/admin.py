from django.contrib import admin
from .models import Categoria, Perfil, Pergunta, UsuarioResposta

admin.site.register(Categoria)
admin.site.register(UsuarioResposta)
admin.site.register(Perfil)
admin.site.register(Pergunta)
