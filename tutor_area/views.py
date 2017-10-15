from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor, Aluno, Tutor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from turmas.models import Turma
from disciplinas.models import Disciplina
from django.http import HttpResponseRedirect
from django.contrib import messages
from turmas.forms import TurmaForm

# Create your views here.
@login_required
def index(request):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	context_dict = {'usuario': usuario}
	if not request.user.is_authenticated :
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
	verificarUser = verificarUsuario(request)
	return render(request, verificarUser ,context=context_dict)


def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'

def todasTurmas(request):
	user = request.user
	usuario = Tutor.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		turmas = Turma.objects.filter(tutor=usuario)
		return render(request, 'tutor_area/todasTurmas.html', {'turmas': turmas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)

def turmaArea(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all()
	return render(request, 'tutor_area/turmaArea.html', {'turma': turma, 'alunos': alunos, 'usuario':usuario})

def listAlunos(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all()
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	return render(request, 'tutor_area/listAlunos.html', context=context)
