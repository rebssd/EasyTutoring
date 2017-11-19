from django.shortcuts import render
from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor, Aluno, Tutor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from turmas.models import Turma
from .models import Post, Comentario
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
from django import forms

from django.template.loader import render_to_string
from django.http import HttpResponse
from resultados.models import Resultado
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core import serializers
from datetime import datetime
# Create your views here.
def show(request,turma_id):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	template = templates(request)
	turma = Turma.objects.get(pk=turma_id)
	p = Post.objects.filter(turma_id=turma).order_by('date').reverse()
	paginator = Paginator(p, 3)
	comentarios = Comentario.objects.all()
	data = datetime.now
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			descricao = form.cleaned_data['descricao']
			anexo = form.cleaned_data['anexo']
			post = Post(titulo = titulo, descricao=descricao, anexo=anexo, turma = turma, usuario = usuario)
			post.save()
			form = PostForm()
			messages.add_message(request, messages.INFO, 'Notícia cadastrada com sucesso.')
			return render(request,'forum/show.html', {'data':data,'comentarios':comentarios,'form':form,'usuario':usuario,'turma':turma,'template':template,'posts':posts})
	messages.add_message(request, messages.ERROR, 'Não foi possível cadastrar a notícia.')
	form = PostForm()
	context= {'data':data,'turma': turma, 
	'usuario':usuario,
	'template': template,
	'posts':posts,
	'form':form,
	'comentarios':comentarios,
	}

	return render(request,'forum/show.html',context=context)

def new(request,turma_id):
	template = templates(request)
	user = request.user
	usuario = Usuario.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	posts = Post.objects.filter(turma_id=turma)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			descricao = form.cleaned_data['descricao']
			anexo = form.cleaned_data['anexo']
			post = Post(titulo = titulo, descricao=descricao, anexo=anexo, turma = turma, usuario = usuario)
			post.save()
			messages.add_message(request, messages.INFO, 'Notícia cadastrada com sucesso.')
			return  render(request, 'forum/show.html', {'usuario':usuario,'turma':turma,'template':template,'posts':posts})
	form = PostForm()
	return render(request, 'forum/new.html', {'form': form,'turma':turma,'template':template})

def cadastrar_comentario(request):
	if request.is_ajax():
		usuario_id = request.GET.get('usuario','')
		post_id = request.GET.get('post','')
		text = request.GET.get('text','')
		usuario = Usuario(pk=usuario_id)
		post = Post(pk=post_id)
		comentario = Comentario(post=post,usuario=usuario,descricao=text)
		comentario.save()
		comentarios = Comentario.objects.filter(post=post)
		context={
		'post':post,
		'comentarios':comentarios,
		}
		html = render_to_string('forum/coments.html', context=context)
		return HttpResponse(html)
def excluir_post(request):
	if request.is_ajax():
		usuario_id = request.GET.get('usuario','')
		post_id = request.GET.get('post','')
		post = Post(pk=post_id)
		try:
			post.delete()
			messages.add_message(request, messages.INFO, 'Notícia deletada com sucesso.')
			exists = {
				'deletou': True
			}

		except:
			messages.add_message(request, messages.INFO, 'Não foi possível deletar a notícia.')
			exists = {
				'deletou': False
			}
		return JsonResponse(exists)

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

def coments(request,post_id):
	post = Post.objects.get(pk=post_id)
	comentarios = post.comentarios.all()

	context={
	'post': post,
	'comentarios':comentarios,
	}
	html = render_to_string('forum/coments.html', context=context)
	return HttpResponse(html)
