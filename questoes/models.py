from django.db import models
from assuntos.models import Assunto

# Create your models here.
class Questao(models.Model):
	enunciado = models.CharField(max_length=200,null=True)
	assunto = models.ForeignKey(Assunto)
	letra_a = models.CharField(max_length=200)
	letra_b = models.CharField(max_length=200)
	letra_c = models.CharField(max_length=200)
	letra_d = models.CharField(max_length=200)
	resposta = models.CharField(max_length=200)
	observacao = models.CharField(max_length=200)

	def __str__(self):
		return self.enunciado
