from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor, Aluno, Tutor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from .models import Turma
from disciplinas.models import Disciplina
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import TurmaForm
# Create your views here.
@login_required
def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.method == 'POST':
		form = TurmaForm(request.POST)
		if form.is_valid():
			codigo = form.cleaned_data['codigo']
			disciplina = form.cleaned_data['disciplina']
			tutor = form.cleaned_data['tutor']
			alunos = form.cleaned_data['alunos']
			nova_turma = Turma(codigo=codigo, disciplina=disciplina,tutor=tutor, professor=usuario)
			nova_turma.save()
			nova_turma.alunos = alunos
			nova_turma.save()
			messages.add_message(request, messages.INFO, 'Turma cadastrada com sucesso.')
			return HttpResponseRedirect('/professor_area/index.html')
		else:
			messages.add_message(request, messages.ERROR, 'Não foi possível cadastrar à turma.')

	form = TurmaForm()
	return render(request, 'turmas/new.html', {'form': form, 'usuario':usuario})
