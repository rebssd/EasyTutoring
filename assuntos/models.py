from django.db import models
from disciplinas.models import Disciplina

# Create your models here.
class Assunto(models.Model):
	nome = models.CharField(max_length=150)
	disciplina = models.ForeignKey(Disciplina)

	def __str__(self):
		return self.nome

