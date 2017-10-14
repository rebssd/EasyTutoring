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
from django.http import HttpResponse
from django.http import JsonResponse
import json

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
			# alunos = form.cleaned_data['alunos']
			nova_turma = Turma(codigo=codigo, disciplina=disciplina,tutor=tutor, professor=usuario)
			# nova_turma.save()
			# nova_turma.alunos = alunos
			nova_turma.save()
			messages.add_message(request, messages.INFO, 'Turma cadastrada com sucesso.')
			return HttpResponseRedirect('/professor_area/index.html')
		else:
			messages.add_message(request, messages.ERROR, 'Não foi possível cadastrar à turma.')

	form = TurmaForm()
	return render(request, 'turmas/new.html', {'form': form, 'usuario':usuario})

def todasTurmas(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	if request.user.has_perm('usuarios.disciplina'):
		t = Turma.objects.all()
		turmas=[]
		for turma in t :
			if turma.professor.id == usuario.id:
				turmas.append(turma)
		return render(request, 'turmas/todasTurmas.html', {'turmas': turmas, 'usuario': usuario})
	else:
		verificaUsuario = verificarUsuario(request)
		return render(request, verificaUsuario)

@login_required
def edit(request,turma_id):
	user = request.user
	usuario = Professor.objects.get(user=user)
	turma = Turma.objects.get(pk=turma_id)
	if request.method == "POST":
		form = TurmaForm(request.POST )
		if form.is_valid():
			codigo = form.cleaned_data['codigo']
			disciplina = form.cleaned_data['disciplina']
			tutor = form.cleaned_data['tutor']
			# alunos = form.cleaned_data['alunos']
			turma.codigo = codigo
			turma.disciplina = disciplina
			turma.tutor = tutor
			# turma.alunos = alunos
			messages.add_message(request, messages.INFO, 'Turma atualizada com sucesso.')
			turma.save()
			return redirect('/turmas/todasTurmas.html')
		else:
			messages.add_message(request, messages.ERROR, 'Não foi possível atualizar.')
	else:
		dados_turma = {'codigo': turma.codigo, 'disciplina': turma.disciplina, 'tutor':turma.tutor, 'alunos':turma.alunos.all()}
		form = TurmaForm(initial=dados_turma)
	return render(request, 'turmas/edit.html', {'form': form, 'turma':turma, 'usuario':usuario})



def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'


 
def autocomplete(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    alunos = Aluno.objects.filter(nome_completo__istartswith=q)
    results = []
    for aluno in alunos:
      aluno_json = {}
      aluno_json = aluno.nome_completo
      results.append(aluno_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def adicionarAlunos(request):
	if request.is_ajax():
		nome = request.GET.get('nome','')
		try:
			aluno = Aluno.objects.get(nome_completo=nome)
			turma = request.GET.get('turma','')
			turmas = Turma.objects.get(pk=turma)
			turmas.alunos.add(aluno)
			turmas.save()
			exists = {
			'cadastrado': True,
			'message': 'O usuário foi adicionado à turma'
			}
		except:
			exists = {
			'cadastrado': False,
			'message': 'Não existem alunos com esse nome.'
			}

	else:
		exists = {
		'cadastrado': False,
		'message': 'oi'
		}
	return JsonResponse(exists)

