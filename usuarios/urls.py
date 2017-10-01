from django.conf.urls import url

from . import views

app_name = 'usuarios'
urlpatterns = [
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^new', views.new, name='new'),
    url(r'^arearestrita', views.restricted_area, name='restricted_area'),
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^validate_username', views.validate_username, name='validate_username'),
    url(r'^validate_email', views.validate_email, name='validate_email'),
    url(r'^validate_matricula', views.validate_matricula, name='validate_matricula'),
]