from django.shortcuts import render, redirect

from .services.curso_service import CursoService
from .services.curso_service_impl import CursoServiceImpl

from .forms import CursoForm, EstudanteForm

from .services.estudante_service import EstudanteService
from .services.estudante_service_impl import EstudanteServiceImpl

estudante_service: EstudanteService = EstudanteServiceImpl()
curso_service: CursoService = CursoServiceImpl()

def home(request):
  return render(request, 'home.html')

def cadastrar_estudante(request):
  if request.method == 'POST':
    estudante_saved = estudante_service.save_estudante(form=EstudanteForm(request.POST))
    if estudante_saved:      
      estudante = {}
      for p in request.POST:
          estudante[p] = request.POST[p]

      return render(request, 'estudante_page.html', { 'estudante': estudante })

  form = EstudanteForm()

  return render(request, 'estudante_form.html', { 'form': form })

def listar_estudantes(request):
  estudantes = estudante_service.get_all_estudantes()

  return render(request, 'estudante_list.html', { 'estudantes': estudantes })

def listar_estudantes_por_curso(request):
  estudantes_by_curso = estudante_service.get_estudantes_order_by_curso()

  return render(request, 'estudantes_by_curso.html', { 'estudantes_by_curso': estudantes_by_curso })

def listar_estudantes_por_linguagem(request):
  estudantes_by_linguagem = estudante_service.get_estudantes_order_by_linguagem()

  return render(request, 'estudantes_by_linguagem.html', { 'estudantes_by_linguagem': estudantes_by_linguagem })

def detalhes_estudante(request, id):
  estudante = estudante_service.get_estudante_by_id(id)
  print(estudante)

  return render(request, 'estudante_details.html', { 'estudante': estudante })

def deletar_estudante(request, id):
  estudante_service.delete_estudante(id)

  return redirect('estudante_list')

def criar_curso(request):
  if request.method == 'POST':
    curso_saved = curso_service.save_curso(form=CursoForm(request.POST))
    if curso_saved:
      return redirect('curso_list')

  form = CursoForm()

  return render(request, 'curso_form.html', { 'form': form })

def listar_curso(request):
  cursos = curso_service.get_all_cursos()

  return render(request, 'curso_list.html', { 'cursos': cursos })

