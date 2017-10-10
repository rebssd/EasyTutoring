from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsuariosForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Tutor, Professor, Aluno
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission

# Create your views here.
def index(request):
# mostra as últimas 5 “poll questions”
    return render(request, 'usuarios/index.html')

def new(request):
	template_name = 'usuarios/new.html'
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
			if tipo == 'tutor' :
				new_profile = Tutor(user=new_user, nome_completo=nome_completo, tipo=tipo,  matricula=matricula, curso=curso,img=img,thumb=img)
				permission = Permission.objects.get(codename='pode_acessar_area_tutor')
				new_user.user_permissions.add(permission)
			elif tipo == 'aluno' :
				new_profile = Aluno(user=new_user, nome_completo=nome_completo, tipo=tipo,  matricula=matricula, curso=curso,img=img,thumb=img)
				permission = Permission.objects.get(codename='pode_acessar_area_aluno')
				new_user.user_permissions.add(permission)
			else :
				new_profile = Professor(user=new_user, nome_completo=nome_completo, tipo=tipo,  matricula=matricula, curso=curso,img=img,thumb=img)
				permission = Permission.objects.get(codename='pode_acessar_area_professor')
				new_user.user_permissions.add(permission)
			new_profile.save()
			return HttpResponseRedirect('index.html')
		else:
			context={ 'form': form, 'erros': True}
			return render(request, 'usuarios/new.html', context=context)

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
				context = {'erro': True, 
				'mensagem_de_erro': "Username ou Senha Incorretos", 
				'form': form}
				return render(request, 'usuarios/login.html', context=context)
	else:
		form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'usuarios/login.html', context=context_dict)

@login_required
def restricted_area(request):
	return render(request, 'usuarios/arearestrita.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('index.html')

def validate_username(request):
    username = request.GET.get('username', None)
    exist_user = {
        'users': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(exist_user)

def validate_email(request):
    email = request.GET.get('email', None)
    exist_email = {
        'emails': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(exist_email)

def validate_matricula(request):
    matricula = request.GET.get('matricula', None)
    exist_matricula = {
        'matriculas': Usuario.objects.filter(matricula__iexact=matricula).exists()
    }
    return JsonResponse(exist_matricula)
