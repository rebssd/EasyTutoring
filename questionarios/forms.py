from django import forms
from .models import Questionario
from disciplinas.models import Disciplina
from usuarios.models import Tutor,Aluno,Professor
from django.forms import ModelForm
from questoes.models import Questao
from assuntos.models import Assunto

class QuestionarioForm(forms.Form):
	codigo = forms.CharField( max_length=50)
	disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all().order_by('nome'))
	questoes = forms.ModelMultipleChoiceField(queryset=Questao.objects.all().order_by('enunciado'))

	def is_valid(self):
		valid = True
		if not super(QuestionarioForm, self).is_valid():
			self.adiciona_erro('Não foi possível cadastrar a turma!')
			valid = False
		return valid
	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

