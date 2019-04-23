from django.db import models

# Create your models here.
from Movies.models import Movie


class Reward(models.Model):
    name = models.CharField(max_length=50, blank=False)
    icon = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class MovieReward(models.Model):
    reward = models.ForeignKey('Reward', default='')
    for_movie = models.ForeignKey('Movies.Movie', default='')
    for_what = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.reward.__str__()


class PersonReward(models.Model):
    reward = models.ForeignKey('Reward', default='')
    for_person = models.ForeignKey('Persons.Person', default='')
    for_what = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.reward.__str__()
