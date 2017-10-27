from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from turmas.models import Turma
from disciplinas.forms import DisciplinaForm
from .models import Questionario
from .forms import QuestionarioForm
from questoes.forms import QuestaoForm
from questoes.models import Questao
from assuntos.models import Assunto
from assuntos.forms import AssuntoForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.template.loader import render_to_string

def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		if request.method == 'POST':
			form = QuestionarioForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				turma = form.cleaned_data['turma']
				questionario = Questionario(codigo=codigo,turma=turma,professor=usuario)
				questionario.save()
				messages.add_message(request, messages.INFO, 'Questionario cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Questionario já cadastrada.')

	form = QuestionarioForm()
	return render(request, 'questionarios/new.html', {'form': form, 'usuario':usuario})

def todosQuestionarios(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	questionarios = Questionario.objects.all()
	return render(request,'questionarios/todosQuestionarios.html',{'usuario':usuario,'questionarios':questionarios})

def assunto(request,questionario_id):
	a = request.GET.get('assunto', '')
	q = request.GET.get('questionario','')
	questionario = Questionario.objects.get(pk=questionario_id)
	assunto = Assunto.objects.get(nome=a)
	questoes = Questao.objects.filter(assunto_id=assunto)
	html = render_to_string('questionarios/questoes.html',{'assunto':assunto, 'questionario':questionario,'questoes':questoes})
	return HttpResponse(html)


def cadastrarQuestoes(request,questionario_id):
	user = request.user
	usuario = Professor.objects.get(user=user)
	questionario = Questionario.objects.get(pk=questionario_id)
	turma = questionario.turma
	disciplina = turma.disciplina
	assuntos = Assunto.objects.filter(disciplina_id=disciplina)
	# dados = {'codigo': questionario.codigo,'assunto':questionario.assunto ,'disciplina': questionario.disciplina, 'professor':questionario.professor, 'questoes':questionario.questoes.all()}

	return render(request, 'questionarios/cadastrarQuestoes.html', {'questionario':questionario,'assuntos':assuntos,'usuario':usuario})


def questoes(request,assunto_id,questionario_id):
	assunto = Assunto.objects.get(pk=assunto_id)
	questionario= Questionario.objects.get(pk=questionario_id)
	questoes = Questao.objects.filter(assunto_id=assunto)
	return render(request,'questionarios/questoes.html',{'assunto':assunto,'questionario':questionario,'questoes':questoes})

def addquestao(request,questionario_id):
	try:
		q = request.GET.get('question','')
		questao = Questao.objects.get(pk=q)
		quest = request.GET.get('questionario','')
		questionario = Questionario.objects.get(pk=quest)
		questionario.questoes.add(questao)
		questionario.save()
		exists = {
		'cadastrado': True,
		'message': 'Questão cadastrada com sucesso.'
		}
	except:
		exists = {
		'cadastrado': False,
		'message': 'Não foi possível cadastrar à questão.'
		}
	return JsonResponse(exists)

def show(request,questionario_id):
	user = request.user
	usuario = Professor.objects.get(user=user)
	questionario = Questionario.objects.get(pk=questionario_id)
	questoes = questionario.questoes.all()
	context = {'usuario':usuario,'questionario':questionario, 'questoes':questoes}
	return render(request,'questionarios/show.html',context=context)
