from abc import abstractmethod
from dataclasses import dataclass
from ..repositories.student_repository import StudentRepository

@dataclass
class StudentService:
    student_repository: StudentRepository

    @abstractmethod
    def save_student(self, student):
        pass

    @abstractmethod
    def delete_student(self, student):
        pass

    abstractmethod
    def get_students(self):
        pass

    @abstractmethod
    def get_student(self, student_id):
        pass