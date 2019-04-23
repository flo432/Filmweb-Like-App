from django.db import models
from Movies.models import Movie
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)

    def __unicode__(self):
        return self.name


class MovieGenre(models.Model):
    genre = models.ForeignKey('Genre', default='')
    for_movie = models.ForeignKey('Movies.Movie', default='')

    def __unicode__(self):
        return self.genre.__str__()