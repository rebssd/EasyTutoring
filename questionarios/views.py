from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from disciplinas.forms import DisciplinaForm
from .models import Questionario
from .forms import QuestionarioForm
from assuntos.models import Assunto
from assuntos.forms import AssuntoForm
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
				disciplina = form.cleaned_data['disciplina']
				questoes = form.cleaned_data['questoes']
				questionario = Questionario(codigo=codigo,disciplina=disciplina,professor=usuario)
				questionario.save()
				questionario.questoes = questoes
				questionario.save()
				messages.add_message(request, messages.INFO, 'Questionario cadastrada com sucesso.')
				return HttpResponseRedirect('/professor_area/index.html')
			else:
				messages.add_message(request, messages.ERROR, 'Questionario já cadastrada.')

	form = QuestionarioForm()
	return render(request, 'questionarios/new.html', {'form': form, 'usuario':usuario})

def todosQuestionarios(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	questionarios = Questionario.objects.all()
	return render(request,'questionarios/todosQuestionarios.html',{'usuario':usuario,'questionarios':questionarios})

def assunto(request):
    assunto = request.GET.get('assunto', None)
    questoes = Question.objects.filter(assunto_ixact=assunto)
    questoes_assunto = {
        'questoes': questoes
    }
    return JsonResponse(questoes_assunto)

def cadastrarQuestoes(request,questionario_id):
	user = request.user
	usuario = Professor.objects.get(user=user)
	questionario = Questionario.objects.get(pk=questionario_id)
	disciplina = questionario.disciplina
	assuntos = Assunto.objects.filter(disciplina_id=disciplina)
	# dados = {'codigo': questionario.codigo,'assunto':questionario.assunto ,'disciplina': questionario.disciplina, 'professor':questionario.professor, 'questoes':questionario.questoes.all()}
	return render(request, 'questionarios/cadastrarQuestoes.html', {'questionario':questionario,'assuntos':assuntos, 'usuario':usuario})


