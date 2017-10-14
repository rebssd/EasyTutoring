from django import forms
from .models import Turma
from disciplinas.models import Disciplina
from usuarios.models import Tutor,Aluno
from django.forms import ModelForm

class TurmaForm(forms.Form):
	codigo = forms.CharField(label='codigo', max_length=150)
	disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all().order_by('nome'))
	tutor = forms.ModelChoiceField(queryset=Tutor.objects.all().order_by('nome_completo'))
	# alunos = forms.ModelMultipleChoiceField(queryset=Aluno.objects.all().order_by('nome_completo'))

	def is_valid(self):
		valid = True
		if not super(TurmaForm, self).is_valid():
			self.adiciona_erro('Não foi possível cadastrar a turma!')
			valid = False
		return valid
