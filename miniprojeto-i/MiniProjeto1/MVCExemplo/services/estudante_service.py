from abc import abstractmethod

from ..forms import EstudanteForm

class EstudanteService():
  @abstractmethod
  def get_all_estudantes(self):
    pass

  @abstractmethod
  def save_estudante(self, form: EstudanteForm):
    pass

  @abstractmethod
  def get_estudante_by_id(self, id):
    pass

  @abstractmethod
  def delete_estudante(self, id):
    pass

  @abstractmethod
  def get_estudantes_order_by_curso(self, curso):
    pass

  @abstractmethod
  def get_estudantes_order_by_linguagem(self, linguagem):
    pass