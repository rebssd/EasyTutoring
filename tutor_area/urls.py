from django.conf.urls import url

from . import views

app_name = 'tutor_area'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^todasTurmas', views.todasTurmas, name='todasTurmas'),
    url(r'^turmaArea/(?P<turma_id>[0-9]+)/$', views.turmaArea, name='turmaArea'),
    url(r'^listAlunos/(?P<turma_id>[0-9]+)/$', views.listAlunos, name='listAlunos'),]

