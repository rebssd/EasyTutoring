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
from questionarios.models import Questionario
from questionarios.forms import QuestionarioForm
from questoes.forms import QuestaoForm
from questoes.models import Questao
from assuntos.models import Assunto
from assuntos.forms import AssuntoForm
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.http import HttpResponse

@login_required
def index(request):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	context_dict = {'usuario': usuario}
	if not request.user.is_authenticated :
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
	verificarUser = verificarUsuario(request)
	return render(request, verificarUser ,context=context_dict)

@login_required
def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'
@login_required
def todasTurmas(request):
	user = request.user
	usuario = Aluno.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_aluno'):
		turmas = Turma.objects.filter(alunos__id=usuario.id)
		return render(request, 'aluno_area/todasTurmas.html', {'turmas': turmas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)

def turmaArea(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all()
	return render(request, 'aluno_area/turmaArea.html', {'turma': turma, 'alunos': alunos, 'usuario':usuario})

def listAlunos(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all()
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	return render(request, 'aluno_area/listAlunos.html', context=context)

def listQuestionarios(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	professor= turma.professor
	questionarios = Questionario.objects.filter(professor_id=professor,turma_id=turma)
	context= {'questionarios':questionarios,
	'usuario':usuario,
	'turma':turma}
	return render(request,'aluno_area/listQuestionarios.html',context=context)

def responderQuestionario(request,turma_id,questionario_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	questionario = Questionario.objects.get(pk=questionario_id)
	questoes = questionario.questoes.all()
	context= {'questionario':questionario,
	'usuario':usuario,
	'turma':turma,
	'questoes':questoes}
	return render(request,'aluno_area/responderQuestionario.html',context=context)

def verficarRespostas(request,turma_id,questionario_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	questionario = Questionario.objects.get(pk=questionario_id)
	questoes = questionario.questoes.all()
	results = request.POST.getlist('results[]')
	ids = request.POST.getlist('ids[]')
	questoes_erradas =  []
	for id in range(len(ids)):
		q= Questao.objects.get(pk=ids[id])
		resposta = results[id]
		if q.resposta != resposta:
			questoes_erradas.append(q)
	context= {'results':results,'turma':turma,'questionario':questionario, 'questoes_erradas':questoes_erradas}
	html = render_to_string('aluno_area/verficarRespostas.html', context=context)
	return HttpResponse(html)
