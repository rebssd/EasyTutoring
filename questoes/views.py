from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from disciplinas.forms import DisciplinaForm
from .models import Questao
from .forms import QuestaoForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		if request.method == 'POST':
			form = QuestaoForm(request.POST)
			if form.is_valid():
				enunciado = form.cleaned_data['enunciado']
				assunto = form.cleaned_data['assunto']
				letra_a = form.cleaned_data['letra_a']
				letra_b = form.cleaned_data['letra_b']
				letra_c = form.cleaned_data['letra_c']
				letra_d = form.cleaned_data['letra_d']
				resposta = form.cleaned_data['resposta']
				observacao = form.cleaned_data['observacao']
				questao = Questao(enunciado=enunciado,assunto=assunto,letra_a=letra_a,letra_b=letra_b,letra_c=letra_c,letra_d=letra_d,resposta=resposta,observacao=observacao)
				questao.save()
				messages.add_message(request, messages.INFO, 'Questão cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Questão já cadastrada.')

	form = QuestaoForm()
	return render(request, 'questoes/new.html', {'form': form, 'usuario':usuario})
