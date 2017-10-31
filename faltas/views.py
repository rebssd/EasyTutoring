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
	alunos = turma.alunos.all()
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	return render(request,'faltas/new.html',context=context)


def cadastrarFrequencia(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	alunos = turma.alunos.all()
	frequencia = request.POST.getlist('frequencia[]')
	alunos_id = request.POST.getlist('alunos[]')
	for i in range(len(alunos_id)):
		aluno = Aluno.objects.get(pk=alunos[i])
		if (frequencia[i] == "Presente") :
			presenca = Falta(alunos=aluno, turmas=turma, presenca=True)
		else:
			presenca = Falta(alunos=aluno,turmas=turma,presenca=False)
		presenca.save()
	context= {'turma': turma, 
	'alunos': alunos, 
	'usuario':usuario}
	return render (request,'faltas/cadastrarFrequencia.html', context=context)
