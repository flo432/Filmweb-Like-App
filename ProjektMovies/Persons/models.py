from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Movies.models import Movie


class Person(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    birth_date = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    poster = models.URLField(blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Actor(models.Model):
    actor = models.ForeignKey('Person', default='')
    in_movie = models.ForeignKey('Movies.Movie', default='')
    character = models.CharField(max_length=120, blank=False)

    def __unicode__(self):
        return self.actor.__str__()


class Director(models.Model):
    director = models.ForeignKey('Person', default='')
    in_movie = models.ForeignKey('Movies.Movie', default='')

    def __unicode__(self):
        return self.director.__str__()


class CommentPerson(models.Model):
    user = models.ForeignKey(User, default='')
    for_person = models.ForeignKey('Person', default='')
    text = models.CharField(max_length=250, blank=False)

    def __unicode__(self):
        return self.for_person.__str__()
