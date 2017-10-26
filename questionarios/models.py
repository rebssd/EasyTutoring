from django.db import models
from turmas.models import Turma
from usuarios.models import Professor
from usuarios.models import Tutor
from usuarios.models import Aluno
from questoes.models import Questao
# Create your models here.
class Questionario(models.Model):
	codigo = models.CharField(max_length=50)
	turma = models.ForeignKey(Turma,null=True)
	professor = models.ForeignKey(Professor)
	questoes = models.ManyToManyField(Questao)
