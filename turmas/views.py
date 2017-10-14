from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor, Aluno, Tutor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from .models import Turma
from disciplinas.models import Disciplina
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import TurmaForm
# Create your views here.
@login_required
def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.method == 'POST':
		form = TurmaForm(request.POST)
		if form.is_valid():
			codigo = form.cleaned_data['codigo']
			disciplina = form.cleaned_data['disciplina']
			tutor = form.cleaned_data['tutor']
			alunos = form.cleaned_data['alunos']
			nova_turma = Turma(codigo=codigo, disciplina=disciplina,tutor=tutor, professor=usuario)
			nova_turma.save()
			nova_turma.alunos = alunos
			nova_turma.save()
			messages.add_message(request, messages.INFO, 'Turma cadastrada com sucesso.')
			return HttpResponseRedirect('/professor_area/index.html')
		else:
			messages.add_message(request, messages.ERROR, 'Não foi possível cadastrar à turma.')

	form = TurmaForm()
	return render(request, 'turmas/new.html', {'form': form, 'usuario':usuario})

def todasTurmas(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.disciplina'):
		t = Turma.objects.all()
		turmas=[]
		for turma in t :
			if turma.professor.id == usuario.id:
				turmas.append(turma)
		return render(request, 'turmas/todasTurmas.html', {'turmas': turmas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)


def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'


