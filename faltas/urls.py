from django.conf.urls import url

from . import views

app_name = 'faltas'
urlpatterns = [
    url(r'^new/(?P<turma_id>[0-9]+)/$', views.new, name='new'),
    url(r'^new/(?P<turma_id>[0-9]+)/cadastrarFrequencia', views.cadastrarFrequencia, name='cadastrarFrequencia'),
    url(r'^dadosFrequencia/(?P<turma_id>[0-9]+)/$', views.dadosFrequencia, name='dadosFrequencia'),
    url(r'^faltaAluno/(?P<turma_id>[0-9]+)/$', views.faltaAluno, name='faltaAluno'),
    ]
