from django.shortcuts import render
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
from resultados.models import Resultado

# Create your views here.
def show(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	if usuario.tipo == "tutor" :
		template = "tutor_area/turmaArea.html"
	elif usuario.tipo == "professor" :
		template = "professor_area/index.html"
	else:
		template = "aluno_area/turmaArea.html"
	turma = Turma.objects.get(pk=turma_id)
	context= {'turma': turma, 
	'usuario':usuario,
	'template': template}
	return render(request,'forum/show.html',context=context)
