from django.shortcuts import render, redirect

from .repositories.course_repository import CourseRepository

from .repositories.student_repository import StudentRepository

from .services.student_service_impl import StudentServiceImpl
from .services.student_service import StudentService
from .forms.student_form import StudentForm

from .services.course_service_impl import CourseServiceImpl
from .services.course_service import CourseService
from .forms.course_form import CourseForm

from .services.avatar_service import AvatarService
from .services.avatar_service_impl import AvatarServiceImpl
from .repositories.avatar_repository import AvatarRepository
from .forms.avatar_form import AvatarForm

student_service: StudentService = StudentServiceImpl(
    student_repository=StudentRepository()
)

course_service: CourseService = CourseServiceImpl(
  course_repository=CourseRepository()
)

avatar_service: AvatarService = AvatarServiceImpl(
  avatar_repository=AvatarRepository()
)

def menu(request):
  return render(request, 'menu.html')

class StudentViews():
  def student_create(request):
    if request.method == 'POST':
      student_service.save_student(request.POST)
      return redirect('students_list')
    
    return render(request, 'student_form.html', {'form': StudentForm()})

  def student_list(request):
    students = student_service.get_students()
    return render(request, 'student_list.html', {'students': students})

  def student_delete(request, student_id):
    student_service.delete_student(student_id)
    return redirect('students_list')

class CourseViews():
  def course_create(request):
    if request.method == 'POST':
      course_service.save_course(request.POST)
      courses = course_service.get_courses()

      return render(request, 'course_list.html', {'courses': courses})
    
    return render(request, 'course_form.html', {'form': CourseForm()})

  def course_list(request):
    courses = course_service.get_courses()
    return render(request, 'course_list.html', {'courses': courses})

  def course_delete(request, course_id):
    course_service.delete_course(course_id)
    return redirect('course_list')

  def course_update(request, course_id):
    if request.method == 'POST':
      course = course_service.update_course(request_post=request.POST, course_id=course_id)
      return redirect('course_list')
    course = course_service.get_course(course_id)
    return render(request, 'course_form.html', {'form': CourseForm(instance=course)})

class AvatarViews():
  def avatar_create(request):
    if request.method == 'POST':
      avatar_service.save_avatar(request.POST)
      return redirect('avatar_list')
    return render(request, 'avatar_form.html', {'form': AvatarForm()})

  def avatar_list(request):
    avatars = avatar_service.get_avatars()
    return render(request, 'avatar_list.html', {'avatars': avatars})
