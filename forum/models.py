from django.db import models
from turmas.models import Turma
from datetime import date

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=150,null=True)
	descricao = models.CharField(max_length=800,null=True)
	anexo = models.FileField(upload_to='arquivos/',null=True)
	turma = models.ForeignKey(Turma,null=True)
	date= models.DateField(("Date"),default= date.today)


class Comentario(models.Model):
	post = models.ForeignKey(Post)
	descricao = models.CharField(max_length=240)
	date= models.DateField(("Date"),default= date.today)

