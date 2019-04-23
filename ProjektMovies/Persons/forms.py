from django.forms import ModelForm, Textarea
from Persons.models import CommentPerson

__author__ = 'asdflo'


class CommentPersonForm(ModelForm):
    class Meta:
        model = CommentPerson
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={'cols': 40, 'rows': 5}),
        }
