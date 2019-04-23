from django.conf.urls import url

from . import views

__author__ = 'asdflo'

urlpatterns = [
    url(r'^$', views.genres, name='genres'),
    url(r'^genre/(?P<genre_name>[\w ]+)/$', views.genre, name='genre'),
]
