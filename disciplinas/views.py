from django.shortcuts import render
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


def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'


