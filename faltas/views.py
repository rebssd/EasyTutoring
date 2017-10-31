from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from usuarios.models import Usuario, Professor,Aluno
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from faltas.models import Falta
from turmas.models import Turma
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.template.loader import render_to_string

# Create your views here.
def new(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all().order_by('nome_completo')
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	return render(request,'faltas/new.html',context=context)


def cadastrarFrequencia(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all().order_by('nome_completo')
	frequencia = request.POST.getlist('frequencia[]')
	alunos_id = request.POST.getlist('alunos[]')
	for i in range(len(alunos_id)):
		aluno = Aluno.objects.get(pk=alunos[i])
		if (frequencia[i].upper() == "PRESENTE") :
			presenca = Falta(alunos=aluno, turmas=turma, presenca=True)
		else:
			presenca = Falta(alunos=aluno,turmas=turma)
		presenca.save()
	messages.add_message(request, messages.INFO, 'Frequência cadastrada com sucesso.')
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	html = render_to_string('aluno_area/verficarRespostas.html', context=context)
	return HttpResponse(html)

def dadosFrequencia(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all().order_by('nome_completo')
	faltas =[]
	nome_alunos=[]
	for i in range(len(alunos)):
		nome_alunos.append(alunos[i].nome_completo)
		falta = Falta.objects.filter(turmas=turma,alunos=alunos[i],presenca=False)

		count_falta = len(falta)
		faltas.append(count_falta)

	context ={'usuario': usuario,
	'turma':turma,
	'faltas': json.dumps(faltas),
	'nome_alunos': json.dumps(nome_alunos),
	}
	return render(request,'faltas/dadosFrequencia.html',context=context)

def faltaAluno(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	faltas = Falta.objects.filter(turmas=turma,alunos=usuario).order_by('date')
	count_falta = len(Falta.objects.filter(turmas=turma,alunos=usuario,presenca=False))
	context ={'usuario': usuario,
	'turma':turma,
	'faltas': faltas,
	'count_falta':count_falta
	}
	return render(request,'faltas/faltaAluno.html',context=context)