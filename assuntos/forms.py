from django import forms
from disciplinas.models import Disciplina
from django.forms import ModelForm

class AssuntoForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=150)
	disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all().order_by('nome'))

	def is_valid(self):
		valid = True
		if not super(AssuntoForm, self).is_valid():
			self.adiciona_erro('Assunto já cadastrado.')
			valid = False
		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
