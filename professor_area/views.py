from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario, Professor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	context_dict = {'usuario': usuario}
	# if not request.user.is_authenticated:
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
	else:
		verificarUser = verificarUsuario(request)
		return render(request, verificarUser ,context=context_dict)


def verificarUsuario(request):
	if request.user.has_perm('usuarios.pode_acessar_area_professor'):
		return 'professor_area/index.html'
	elif request.user.has_perm('usuarios.pode_acessar_area_tutor'):
		return  'tutor_area/index.html'
	else:
		return 'aluno_area/index.html'



