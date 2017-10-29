from django.conf.urls import url

from . import views

app_name = 'resultados'
urlpatterns = [
    url(r'^index/(?P<questionario_id>[0-9]+)/$', views.index, name='index'),
    ]