from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import numpy as np


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False)
    org_title = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    duration = models.DurationField(blank=True)
    relase_date = models.DateField(blank=False)
    poster = models.URLField(blank=True)
    trailer = models.URLField(blank=True)

    def average_rating(self):
            all_ratings = map(lambda x: x.rate, self.ratemovie_set.all())
            return np.mean(all_ratings)

    def __unicode__(self):
        return self.title


class CommentMovie(models.Model):
    user = models.ForeignKey(User, default='')
    for_movie = models.ForeignKey('Movie', default='')
    text = models.CharField(max_length=250, blank=False)

    def __unicode__(self):
        return self.for_movie.__str__()


class RateMovie(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    user = models.ForeignKey(User, default='')
    for_movie = models.ForeignKey('Movie', default='')
    rate = models.IntegerField(choices=RATING_CHOICES)

    def __unicode__(self):
        return self.for_movie.__str__()
