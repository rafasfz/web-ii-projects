from django.contrib import admin

from .models import Curso, Estudante, SistemaOperacional

class SistemaOperacionalAdmin(admin.ModelAdmin):
  list_display = ('nome',)

class CursoAdmin(admin.ModelAdmin):
  list_display = ('nome',)

class EstudantesAdmin(admin.ModelAdmin):
  list_display = ('primeiroNome', 'ultimoNome', 'curso', 'linguagem', 'email')

admin.site.register(SistemaOperacional, SistemaOperacionalAdmin)
admin.site.register(Estudante, EstudantesAdmin)
admin.site.register(Curso, CursoAdmin)