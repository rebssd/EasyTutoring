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


def index(request,questionario_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	questionario = Questionario.objects.get(pk=questionario_id)
	resultados = Resultado.objects.filter(questionario=questionario)
	questoes = questionario.questoes.all()
	num_q =[]
	for i in range(1,len(questoes)+1):
		q1 = str(i)
		num_q.append("Questao 0"+q1)
	erros_por_questao =[]
	erros=0
	for questao in questoes:
		for x in range(len(resultados)):
			erradas = resultados[x].questoes_erradas.all()
			if questao in erradas:
				erros+=1
		erros_por_questao.append(erros)
		erros=0

	context = {'usuario':usuario,
	'questionario':questionario,
	'num_q': json.dumps(num_q),
	'erros_por_questao': json.dumps(erros_por_questao),
	}
	return render(request,'resultados/index.html', context)