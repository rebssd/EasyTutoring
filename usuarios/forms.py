from django import forms
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from django.forms.widgets import ClearableFileInput
from easy_thumbnails.widgets import ImageClearableFileInput

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
	img = forms.ImageField(widget=ClearableFileInput)

	def is_valid(self):
		valid = True
		if not super(UsuariosForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados.')
			valid = False

		user_exists = User.objects.filter(username=self.data['login']).exists()

		if user_exists:
			self.adiciona_erro('Usuario ja existente.')
			valid = False
		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)


class LoginForm(forms.Form):
	login = forms.CharField(label='Login', max_length=50)
	senha = forms.CharField(label='Senha', max_length=50,
	widget=forms.PasswordInput())