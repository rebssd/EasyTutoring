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

@login_required
def index(request):
	user = request.user
	usuario = Aluno.objects.get(user=user)
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
	usuario = Aluno.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_aluno'):
		turmas = Turma.objects.filter(alunos__id=usuario.id)
		return render(request, 'tutor_area/todasTurmas.html', {'turmas': turmas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)
