from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('estudante/showForm/', views.cadastrar_estudante),
  path('estudante/getListaEstudantes/', views.listar_estudantes, name='estudante_list'),
  path('estudante/<int:id>/', views.detalhes_estudante),
  path('estudante/<int:id>/delete/', views.deletar_estudante),
  path('estudante/getListaEstudantesByCurso/', views.listar_estudantes_por_curso),
  path('estudante/getListaEstudantesByLinguagem/', views.listar_estudantes_por_linguagem),
  path('curso/showForm/', views.criar_curso),
  path('curso/getListaCursos/', views.listar_curso, name='curso_list'),
]