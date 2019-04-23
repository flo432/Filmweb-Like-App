from django.conf.urls import url

from . import views

__author__ = 'asdflo'

urlpatterns = [
    url(r'^$', views.movies, name='movies'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
    url(r'^movie/(?P<movie_id>[0-9]+)/add_comment/$', 'Movies.views.add_comment', name='add_comment'),
    url(r'^movie/(?P<movie_id>[0-9]+)/add_rating/$', 'Movies.views.add_rating', name='add_rating'),
]