from django.shortcuts import render
from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor, Aluno, Tutor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from turmas.models import Turma
from .models import Post
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
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
	template = templates(request)
	turma = Turma.objects.get(pk=turma_id)
	posts = Post.objects.filter(turma_id=turma)
	context= {'turma': turma, 
	'usuario':usuario,
	'template': template,
	'posts':posts}
	return render(request,'forum/show.html',context=context)

def new(request,turma_id):
	template = ""
	user = request.user
	usuario = Usuario.objects.get(user=user)
	if usuario.tipo == "tutor" :
		template = "tutor_area/turmaArea.html"
	elif usuario.tipo == "professor" :
		template = "professor_area/index.html"
	else:
		template = "aluno_area/turmaArea.html"
	turma = Turma.objects.get(pk=turma_id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			descricao = form.cleaned_data['descricao']
			anexo = form.cleaned_data['anexo']
			post = Post(titulo = titulo, descricao=descricao, anexo=anexo, turma = turma)
			post.save()
			messages.add_message(request, messages.INFO, 'Notícia cadastrada com sucesso.')
			return  render(request, 'forum/show.html', {'turma':turma,'template':template})
	form = PostForm()
	return render(request, 'forum/new.html', {'form': form,'turma':turma,'template':template})


def templates(request):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	if usuario.tipo == "tutor" :
		template = "tutor_area/turmaArea.html"
	elif usuario.tipo == "professor" :
		template = "professor_area/index.html"
	else:
		template = "aluno_area/turmaArea.html"
	return template
