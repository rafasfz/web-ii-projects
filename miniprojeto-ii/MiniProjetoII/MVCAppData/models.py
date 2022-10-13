from django.db import models

class Course(models.Model):
  description = models.CharField(max_length=512, verbose_name='Curso')

  def __str__(self):
    return self.description

class Subject(models.Model):
  description = models.CharField(max_length=512, verbose_name='Disciplina')
  code = models.CharField(max_length=512, verbose_name='Código')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')

  def __str__(self):
    return self.description

class Student(models.Model):
  name = models.CharField(max_length=512, verbose_name='Nome')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso', null=True)
  subjects = models.ManyToManyField(Subject, verbose_name='Disciplinas')

  def __str__(self):
    return self.name

class Avatar(models.Model):
  fantasy_name = models.CharField(max_length=512, verbose_name='Nome Fantasia')
  student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Estudante')