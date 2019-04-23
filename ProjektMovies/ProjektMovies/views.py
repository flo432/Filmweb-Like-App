from django.shortcuts import render

__author__ = 'asdflo'


def home(request):
    return render(request, "base.html", {})
