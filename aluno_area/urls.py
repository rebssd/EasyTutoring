from django.conf.urls import url

from . import views

app_name = 'aluno_area'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^responderQuestionario/(?P<turma_id>[0-9]+)/(?P<questionario_id>[0-9]+)/verficarRespostas', views.verficarRespostas, name='verficarRespostas'),
    url(r'^todasTurmas', views.todasTurmas, name='todasTurmas'),
    url(r'^listQuestionarios/(?P<turma_id>[0-9]+)/$', views.listQuestionarios, name='listQuestionarios'),
    url(r'^responderQuestionario/(?P<turma_id>[0-9]+)/(?P<questionario_id>[0-9]+)/$', views.responderQuestionario, name='responderQuestionario'),
    url(r'^turmaArea/(?P<turma_id>[0-9]+)/$', views.turmaArea, name='turmaArea'),
    url(r'^listAlunos/(?P<turma_id>[0-9]+)/$', views.listAlunos, name='listAlunos'),]
