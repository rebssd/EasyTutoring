from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from turmas.models import Turma
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.template.loader import render_to_string

# Create your views here.
def index(request):

	return render(request,'faltas/new.html')
