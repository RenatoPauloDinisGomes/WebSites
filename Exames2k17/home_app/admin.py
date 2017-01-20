from django.contrib import admin
from .models import Cadeira,Tema,SubTema,Curso

admin.site.register(Cadeira)
admin.site.register(Tema)
admin.site.register(SubTema)
admin.site.register(Curso)