from django.forms import ModelForm
from .models import Curso, Estudante

class EstudanteForm(ModelForm):
  class Meta:
    model = Estudante
    fields = ['primeiroNome', 'ultimoNome', 'linguagem', 'curso', 'email', 'sistemasOperacionais']

class CursoForm(ModelForm):
  class Meta:
    model = Curso
    fields = ['nome']