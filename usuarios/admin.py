from django.contrib import admin
from .models import Usuario, Aluno , Professor, Tutor

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Tutor)

