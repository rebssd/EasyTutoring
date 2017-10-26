from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from disciplinas.forms import DisciplinaForm
from .models import Assunto
from .forms import AssuntoForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.disciplina'):
		if request.method == 'POST':
			form = AssuntoForm(request.POST)
			if form.is_valid():
				nome = (form.cleaned_data['nome']).lower()
				disciplina = form.cleaned_data['disciplina']
				assunto = Assunto(nome=nome, disciplina= disciplina)
				assunto.save()
				messages.add_message(request, messages.INFO, 'Disciplina cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Disciplina já cadastrada.')

	form = AssuntoForm()
	return render(request, 'assuntos/new.html', {'form': form, 'usuario':usuario})
