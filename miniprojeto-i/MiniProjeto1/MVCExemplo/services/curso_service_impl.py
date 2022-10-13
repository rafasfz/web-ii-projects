from .curso_service import CursoService
from ..models import Curso

class CursoServiceImpl(CursoService):
  def get_all_cursos(self):
    cursos = Curso.objects.all()
    cursos = list(cursos)

    return cursos

  def save_curso(self, form):
    if form.is_valid():
      form.save()
      return True

    return False
