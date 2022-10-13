from abc import abstractmethod


class CursoService():
  @abstractmethod
  def get_all_cursos(self):
    pass

  @abstractmethod
  def save_curso(self, form):
    pass