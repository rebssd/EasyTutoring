from django.conf.urls import url

from . import views

app_name = 'usuarios'
urlpatterns = [
    url(r'^login', views.user_login, name='login'),
    url(r'^new', views.new, name='new'),
    url(r'^arearestrita', views.restricted_area, name='restricted_area'),
    url(r'^index', views.index, name='index'),
]