from django.conf.urls import url

from . import views

app_name = 'questionarios'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    ]