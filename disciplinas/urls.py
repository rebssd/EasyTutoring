from django.conf.urls import url

from . import views

app_name = 'disciplinas'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    url(r'^show', views.show, name='show'),
    url(r'^(?P<disciplina_id>[0-9]+)/$', views.edit, name='edit'),]