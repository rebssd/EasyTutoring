from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from disciplinas.forms import DisciplinaForm
from .models import Questionario
from .forms import QuestionarioForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		if request.method == 'POST':
			form = QuestionarioForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				assunto = form.cleaned_data['assunto']
				disciplina = form.cleaned_data['disciplina']
				questoes = form.cleaned_data['questoes']
				questionario = Questionario(codigo=codigo,assunto=assunto,disciplina=disciplina,professor=usuario)
				questionario.save()
				questionario.questoes = questoes
				questionario.save()
				messages.add_message(request, messages.INFO, 'Questionario cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Questionario já cadastrada.')

	form = QuestionarioForm()
	return render(request, 'questionarios/new.html', {'form': form, 'usuario':usuario})
