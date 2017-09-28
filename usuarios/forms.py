from django import forms

class UsuariosForm(forms.Form):
	CHOICES = (('LCC', 'Licenciatura em Ciencia da Computacao'),('SI', 'Sistema de Informacao'),)
	CHOICES_TIPO = (('tutor', 'Tutor'),('aluno', 'Aluno'),('professor', 'Professor'),)
	login = forms.CharField(label='Login', max_length=50)
	senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput())
	email = forms.EmailField(max_length=100)
	nome_completo = forms.CharField(label='nome_completo', max_length=150)
	matricula = forms.CharField(label='Matricula', max_length=20)
	curso = forms.ChoiceField(label='Curso', choices=CHOICES)
	tipo = forms.ChoiceField(label='Tipo', choices=CHOICES_TIPO)


class LoginForm(forms.Form):
	login = forms.CharField(label='Login', max_length=50)
	senha = forms.CharField(label='Senha', max_length=50,
	widget=forms.PasswordInput())