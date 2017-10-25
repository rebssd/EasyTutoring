from django import forms
from .models import Questao
from disciplinas.models import Disciplina
from usuarios.models import Tutor,Aluno,Professor
from django.forms import ModelForm

class QuestaoForm(forms.Form):
	CHOICES = (('a', 'a'),('b', 'b'),('c', 'c'),('d', 'd'))
	enunciado = forms.CharField(max_length=200)
	assunto = forms.CharField(max_length=100)
	letra_a = forms.CharField(max_length=200)
	letra_b = forms.CharField(max_length=200)
	letra_c = forms.CharField(max_length=200)
	letra_d = forms.CharField(max_length=200)
	resposta = forms.ChoiceField(choices=CHOICES,widget=forms.widgets.RadioSelect())
	observacao = forms.CharField(max_length=200)

	def is_valid(self):
		valid = True
		if not super(QuestaoForm, self).is_valid():
			self.adiciona_erro('Não foi possível cadastrar a turma!')
			valid = False
		return valid
	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

