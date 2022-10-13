from ..models import Student

class StudentRepository():
  def save_student(self, form_student):
    student = form_student.save()
    return student
  
  def get_students(self):
    return Student.objects.all()

  def delete_student(self, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()