from django.db import models

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=150,null=True)
	descricao = models.CharField(max_length=800,null=True)
	anexo = models.FileField(upload_to='arquivos/')


class Comentario(models.Model):
	post = models.ForeignKey(Post)
	descricao = models.CharField(max_length=240)

