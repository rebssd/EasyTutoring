from django import forms
from .models import Disciplina
from django.forms import ModelForm


class DisciplinaForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=150)
	class Meta:
		model = Disciplina
		fields = ['nome']
	def is_valid(self):
		valid = True
		if not super(DisciplinaForm, self).is_valid():
			self.adiciona_erro('Disciplina já cadastradaxzczxczxczxcxz.')
			valid = False
		disciplina_exist = Disciplina.objects.filter(nome=(self.data['nome']).lower()).exists()
		if disciplina_exist:
			self.adiciona_erro('Disciplina já cadastrada.')
			valid = False
		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
