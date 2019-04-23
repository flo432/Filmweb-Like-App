from django.forms import ModelForm, Textarea
from Movies.models import CommentMovie, RateMovie

__author__ = 'asdflo'


class CommentMovieForm(ModelForm):
    class Meta:
        model = CommentMovie
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class RateMovieForm(ModelForm):
    class Meta:
        model = RateMovie
        fields = ['rate']