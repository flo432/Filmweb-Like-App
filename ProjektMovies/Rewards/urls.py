from django.conf.urls import url
from . import views
__author__ = 'asdflo'

urlpatterns = [
    url(r'^$', views.rewards, name='rewards'),
    url(r'^reward/(?P<reward_name>[\w ]+)/$', views.reward, name='reward'),
]