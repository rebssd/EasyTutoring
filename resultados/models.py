from django.db import models
from questoes.models import Questao
from questionarios.models import Questionario
from usuarios.models import Aluno

class Resultado(models.Model):
	questoes_erradas = models.ManyToManyField(Questao)
	questionario =  models.ForeignKey(Questionario)
	aluno  = models.ForeignKey(Aluno,null=True)