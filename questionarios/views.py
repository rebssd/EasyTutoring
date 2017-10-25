from django.shortcuts import  get_object_or_404, render,redirect
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from disciplinas.models import Disciplina
from disciplinas.forms import DisciplinaForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def new(request):
	user = request.user
	usuario = Professor.objects.get(user=user)
	return render(request, 'questionarios/new.html', { 'usuario':usuario})
