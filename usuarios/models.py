from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Usuario(models.Model):
	# TOMAR CUIDADO COM ISSO AQUI

	user = models.OneToOneField(User)
	matricula = models.CharField(max_length=20)
	curso = models.CharField(max_length=3)
	tipo = models.CharField(max_length=8, blank=False,null=True)
	nome_completo = models.CharField(max_length=150)

	def __str__(self):
		return self.user.username