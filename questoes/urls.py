from django.conf.urls import url

from . import views

app_name = 'questoes'
urlpatterns = [
    url(r'^new', views.new, name='new'),
    ]