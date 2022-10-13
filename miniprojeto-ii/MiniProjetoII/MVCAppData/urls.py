from django.urls import path
from .views import CourseViews, StudentViews, AvatarViews, menu

urlpatterns = [
  path('', menu),
  path('students/create/', StudentViews.student_create, name='students_create'),
  path('students/delete/<int:student_id>/', StudentViews.student_delete, name='students_delete'),
  path('students/', StudentViews.student_list, name='students_list'),
  path('courses/create/', CourseViews.course_create, name='course_create'),
  path('courses/', CourseViews.course_list, name='course_list'),
  path('courses/delete/<int:course_id>/', CourseViews.course_delete, name='course_delete'),
  path('courses/update/<int:course_id>/', CourseViews.course_update, name='course_update'),
  path('avatars/create/', AvatarViews.avatar_create, name='avatar_create'),
  path('avatars/', AvatarViews.avatar_list, name='avatar_list'),
]
