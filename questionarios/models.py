from django.db import models
from disciplinas.models import Disciplina
from usuarios.models import Professor
from usuarios.models import Tutor
from usuarios.models import Aluno
from questoes.models import Questao
# Create your models here.
class Questionario(models.Model):
	codigo = models.CharField(max_length=50)
	disciplina = models.ForeignKey(Disciplina)
	professor = models.ForeignKey(Professor)
	questoes = models.ManyToManyField(Questao)
