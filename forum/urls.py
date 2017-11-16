from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^show/(?P<turma_id>[0-9]+)/$', views.show, name='show'),
    ]
