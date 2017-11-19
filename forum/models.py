from django.db import models
from turmas.models import Turma
from datetime import date
from usuarios.models import Usuario
# Create your models here.
from django.utils import timezone

class Post(models.Model):
	titulo = models.CharField(max_length=150,null=True)
	descricao = models.CharField(max_length=800,null=True)
	anexo = models.FileField(upload_to='arquivos/',null=True)
	turma = models.ForeignKey(Turma,null=True)
	date= models.DateTimeField(default=timezone.now)
	usuario = models.ForeignKey(Usuario,null=True)
	def __str__(self):
		return self.descricao


class Comentario(models.Model):
	descricao = models.CharField(max_length=240)
	date= models.DateTimeField(default=timezone.now)
	usuario = models.ForeignKey(Usuario,null=True)
	post = models.ForeignKey(Post,null=True)
	def __str__(self):
		return self.descricao
