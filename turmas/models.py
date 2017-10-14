from django.db import models
from disciplinas.models import Disciplina
from usuarios.models import Professor
from usuarios.models import Tutor
from usuarios.models import Aluno
# Create your models here.
class Turma(models.Model):
	codigo = models.CharField(max_length=150)
	disciplina = models.ForeignKey(Disciplina)
	professor = models.ForeignKey(Professor)
	tutor = models.ForeignKey(Tutor)
	alunos = models.ManyToManyField(Aluno)


	def __str__(self):
		return self.codigo

