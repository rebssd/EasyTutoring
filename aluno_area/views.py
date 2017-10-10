from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

@login_required
def index(request):
	user = request.user
	usuario = Usuario.objects.get(user=user)
	context_dict = {'usuario': usuario}
	if not (request.user.is_authenticated or request.user.has_perm('usuarios.pode_acessar_area_aluno')):
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
	return render(request, 'aluno_area/index.html',context=context_dict)