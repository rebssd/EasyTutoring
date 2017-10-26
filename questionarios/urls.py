from django.conf.urls import url

from . import views

app_name = 'questionarios'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    url(r'^todosQuestionarios', views.todosQuestionarios, name='todosQuestionarios'),
    url(r'^(?P<questionario_id>[0-9]+)/$', views.cadastrarQuestoes, name='cadastrarQuestoes'),]