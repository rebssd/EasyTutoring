from django.conf.urls import url

from . import views

app_name = 'questionarios'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    url(r'^(?P<questionario_id>[0-9]+)/addquestao', views.addquestao, name='addquestao'),
    url(r'^(?P<questionario_id>[0-9]+)/assunto', views.assunto, name='assunto'),
    url(r'^todosQuestionarios', views.todosQuestionarios, name='todosQuestionarios'),
    url(r'^(?P<questionario_id>[0-9]+)/$', views.cadastrarQuestoes, name='cadastrarQuestoes'),
    url(r'^questoes/(?P<assunto_id>[0-9]+)/(?P<questionario_id>[0-9]+)/$', views.questoes, name='questoes'),]
