from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
class Usuario(models.Model):
	# TOMAR CUIDADO COM ISSO AQUI

	user = models.OneToOneField(User)
	matricula = models.CharField(max_length=20)
	curso = models.CharField(max_length=3)
	tipo = models.CharField(max_length=8, blank=False,null=True)
	nome_completo = models.CharField(max_length=150)
	img = models.ImageField(upload_to="img/original/", blank=True)
	thumb = ThumbnailerImageField(upload_to="img/thumb/", blank=True,null=True,resize_source=dict(size=(100, 100), sharpen=True))

	def __str__(self):
		return self.user.username


# class Professor(Usuario):
# 	pass

# type(umprofessor)
class Professor(Usuario):
	pass
	class Meta:
		permissions = (
			("pode_acessar_area_professor", "pode acessar area professor"),
			("disciplina","pode fazer o crud de disciplina"),
		)

# type(umprofessor)
class Aluno(Usuario):
	pass
	class Meta:
		permissions= (
			("pode_acessar_area_aluno", "pode acessar area aluno"),
		)
class Tutor(Usuario):
	pass
	class Meta:
		permissions = (
			("pode_acessar_area_tutor", "pode acessar area tutor"),
		)
