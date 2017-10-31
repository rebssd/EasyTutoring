from django.conf.urls import url

from . import views

app_name = 'faltas'
urlpatterns = [
    url(r'^new', views.index, name='new'),
    ]