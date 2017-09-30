from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsuariosForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth import logout


# Create your views here.
def index(request):
# mostra as últimas 5 “poll questions”
    return render(request, 'usuarios/index.html')

def new(request):
	if request.method == 'POST':
		form = UsuariosForm(request.POST, request.FILES)
		if form.is_valid():
			login = form.cleaned_data['login']
			senha = form.cleaned_data['senha']
			email = form.cleaned_data['email']
			nome_completo = form.cleaned_data['nome_completo']
			matricula = form.cleaned_data['matricula']
			curso = form.cleaned_data['curso']
			tipo = form.cleaned_data['tipo']
			img = form.cleaned_data['img']
			new_user = User.objects.create_user(login, email=email, password=senha)
			new_user.save()
			new_profile = Usuario(user=new_user, nome_completo=nome_completo, tipo=tipo,  matricula=matricula, curso=curso,img=img,thumb=img)
			new_profile.save()

			return HttpResponseRedirect('/usuarios/index.html')
	else:
		form = UsuariosForm()
	return render(request, 'usuarios/new.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			form_login = form.cleaned_data['login']
			form_senha = form.cleaned_data['senha']
			user = authenticate(username=form_login, password=form_senha)
			if user is not None:
				login(request,user)
				login_usuario = Usuario.objects.get(user=user)
				if login_usuario.tipo == 'professor':
					return HttpResponseRedirect('/professor_area/index.html')
				elif login_usuario.tipo == 'aluno':
					return HttpResponseRedirect('/aluno_area/index.html')
				else:
					return HttpResponseRedirect('/tutor_area/index.html')
	else:
		form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'usuarios/login.html', context=context_dict)

@login_required
def restricted_area(request):
	return render(request, 'usuarios/arearestrita.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/usuarios/index.html')
