from abc import abstractmethod
from dataclasses import dataclass
from ..repositories.course_repository import CourseRepository

@dataclass
class CourseService:
    course_repository: CourseRepository

    @abstractmethod
    def save_course(self, course):
        pass

    @abstractmethod
    def delete_course(self, course_id):
        pass

    abstractmethod
    def get_courses(self):
        pass

    @abstractmethod
    def get_course(self, course_id):
        pass

    @abstractmethod
    def update_course(self, course_id, request_post):
        pass