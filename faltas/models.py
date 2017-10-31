from django.db import models
from turmas.models import Turma
from usuarios.models import Aluno
from datetime import date


# Create your models here.
class Falta(models.Model):
	turmas = models.ForeignKey(Turma)
	alunos= models.ForeignKey(Aluno)
	date= models.DateField(("Date"),default= date.today)
	presenca = models.BooleanField(default=False)

