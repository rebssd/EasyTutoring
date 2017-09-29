from django.conf.urls import url

from . import views

app_name = 'professor_area'
urlpatterns = [
    url(r'^index', views.index, name='index'),
]