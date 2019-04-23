from django.conf.urls import url
from . import views
__author__ = 'asdflo'


urlpatterns = [
    url(r'^$', views.profile, name='profile'),
]