from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from .models import Disciplina
from .forms import DisciplinaForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
@login_required
def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.disciplina'):
		if request.method == 'POST':
			form = DisciplinaForm(request.POST)
			if form.is_valid():
				nome = (form.cleaned_data['nome']).lower()
				nova_disciplina = Disciplina(nome=nome)
				nova_disciplina.save()
				messages.add_message(request, messages.INFO, 'Disciplina cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Disciplina já cadastrada.')

	form = DisciplinaForm()
	return render(request, 'disciplinas/new.html', {'form': form, 'usuario':usuario})

@login_required
def show(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.disciplina'):
		disciplinas = Disciplina.objects.all()
		return render(request, 'disciplinas/show.html', {'disciplinas': disciplinas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)

@login_required
def edit(request,disciplina_id):
	user = request.user
	usuario = Professor.objects.get(user=user)
	disciplina = Disciplina.objects.get(pk=disciplina_id)
	if request.method == "POST":
		form = DisciplinaForm(request.POST )
		if form.is_valid():
			nome = form.cleaned_data["nome"]
			disciplina.nome=nome
			disciplina.save()
			messages.add_message(request, messages.INFO, 'Disciplina atualizada com sucesso.')
			return redirect('/disciplinas/show.html')
		else:
			messages.add_message(request, messages.ERROR, 'Disciplina já cadastrada.')
	else:
		nome = {"nome": disciplina.nome}
		form = DisciplinaForm(initial=nome)
	return render(request, 'disciplinas/edit.html', {'form': form, 'disciplina':disciplina})


def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'


