from django.conf.urls import url

from . import views

app_name = 'turmas'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    url(r'^todasTurmas', views.todasTurmas, name='todasTurmas'),
    url(r'^(?P<turma_id>[0-9]+)/$', views.edit, name='edit'),]