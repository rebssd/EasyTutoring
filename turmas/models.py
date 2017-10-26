from django.db import models
from disciplinas.models import Disciplina
from usuarios.models import Professor
from usuarios.models import Tutor
from usuarios.models import Aluno
# Create your models here.
class Turma(models.Model):
	codigo = models.CharField(max_length=150)
	disciplina = models.ForeignKey(Disciplina, related_name='disciplinas',null=True)
	professor = models.ForeignKey(Professor, related_name='professores')
	tutor = models.ForeignKey(Tutor, related_name='tutores')
	alunos = models.ManyToManyField(Aluno, related_name='alunos')


	def __str__(self):
		return self.codigo