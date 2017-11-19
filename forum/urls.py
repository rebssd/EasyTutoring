from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^show/(?P<turma_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new/(?P<turma_id>[0-9]+)/$', views.new, name='new'),
    url(r'^cadastrar_comentario', views.cadastrar_comentario, name='cadastrar_comentario'),
    url(r'^coments/(?P<post_id>[0-9]+)/$', views.coments, name='coments'),

    ]
