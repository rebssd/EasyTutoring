from django.conf.urls import url

from . import views

app_name = 'tutor_area'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^todasTurmas', views.todasTurmas, name='todasTurmas'),

]