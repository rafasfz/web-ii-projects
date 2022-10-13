from abc import abstractmethod
from dataclasses import dataclass

from ..forms.student_form import StudentForm
from ..repositories.student_repository import StudentRepository
from .student_service import StudentService

@dataclass
class StudentServiceImpl(StudentService):
    student_repository: StudentRepository
    
    def __init__(self, student_repository):
      self.student_repository = student_repository

    def save_student(self, request_post):
      form_student = StudentForm(request_post)
      if form_student.is_valid():
        student = self.student_repository.save_student(form_student)
        return student
      return None

    def delete_student(self, student_id):
      self.student_repository.delete_student(student_id)

    def get_students(self):
      return self.student_repository.get_students()

    @abstractmethod
    def get_student(self, student_id):
      pass