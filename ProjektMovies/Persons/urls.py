from django.conf.urls import url

from . import views

__author__ = 'asdflo'

urlpatterns = [
    url(r'^$', views.persons, name='persons'),
    url(r'^person/(?P<person_id>[0-9]+)/$', views.person, name='person'),
    url(r'^person/(?P<person_id>[0-9]+)/add_comment/$', 'Persons.views.add_comment', name='add_comment'),
]
