from ..models import Course

class CourseRepository:
  def save_course(self, form_course):
    course = form_course.save()
    return course
  
  def get_courses(self):
    return Course.objects.all()

  def delete_course(self, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()

  def update_course(self, course_id, form_course):
    course = Course.objects.get(id=course_id)
    course.description = form_course.cleaned_data['description']
    course.save()
    return course

  def get_course(self, course_id):
    course = Course.objects.get(id=course_id)
    return course