from ..forms import EstudanteForm
from .estudante_service import EstudanteService
from ..models import Curso, Estudante, Linguagem

class EstudanteServiceImpl(EstudanteService):
  def get_all_estudantes(self):
    estudantes = Estudante.objects.all()
    estudantes = list(estudantes)

    return estudantes

  def save_estudante(self, form: EstudanteForm):
    if form.is_valid():
      form.save()
      return True

    return False

  def get_estudante_by_id(self, id):
    estudante = Estudante.objects.get(id=id)

    return estudante

  def delete_estudante(self, id):
    estudante = Estudante.objects.get(id=id)
    estudante.delete()

    return True

  def get_estudantes_order_by_curso(self):
    cursos = Curso.objects.all()
    cursos = list(cursos)

    estudantes_by_curso = []
    total = 0

    for curso in cursos:
      estudantes = Estudante.objects.filter(curso=curso)
      estudantes = list(estudantes)
      total+=len(estudantes)

      estudantes_by_curso.append({
        'curso': curso,
        'estudantes': estudantes
      })

    return {
      'estudantes_by_curso': estudantes_by_curso,
      'total': total
    }

  def get_estudantes_order_by_linguagem(self):
    linguagens = Linguagem.objects.all()
    linguagens = list(linguagens)

    estudantes_by_linguagem = []
    total = 0

    for linguagem in linguagens:
      estudantes = Estudante.objects.filter(linguagem=linguagem)
      estudantes = list(estudantes)
      total+=len(estudantes)

      estudantes_by_linguagem.append({
        'linguagem': linguagem,
        'estudantes': estudantes
      })

    return {
      'estudantes_by_linguagem': estudantes_by_linguagem,
      'total': total
    }