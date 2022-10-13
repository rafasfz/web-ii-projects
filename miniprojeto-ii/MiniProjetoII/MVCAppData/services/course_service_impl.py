from abc import abstractmethod
from dataclasses import dataclass

from ..forms.course_form import CourseForm
from ..repositories.course_repository import CourseRepository
from .course_service import CourseService

@dataclass
class CourseServiceImpl(CourseService):
    course_repository: CourseRepository
    
    def __init__(self, course_repository):
      self.course_repository = course_repository

    def save_course(self, request_post):
      form_course = CourseForm(request_post)
      if form_course.is_valid():
        course = self.course_repository.save_course(form_course)
        return course
      return None

    def delete_course(self, course_id):
      self.course_repository.delete_course(course_id)

    def get_courses(self):
      return self.course_repository.get_courses()

    def update_course(self, course_id, request_post):
      form_course = CourseForm(request_post)
      if form_course.is_valid():
        course = self.course_repository.update_course(course_id, form_course)
        return course
      return None

    def get_course(self, course_id):
      course = self.course_repository.get_course(course_id)
      return course