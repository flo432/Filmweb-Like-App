from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from Persons.forms import CommentPersonForm
from Rewards.models import PersonReward

from .models import Person, Actor, Director, CommentPerson


# Create your views here.


def persons(request):
    persons = Person.objects.order_by('first_name')
    paginator = Paginator(persons, 5)

    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        "persons": persons,
        'object_list': page,
    }

    return render(request, "persons.html", context)


def person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    movies = Actor.objects.select_related().filter(actor_id=person_id)
    director = Director.objects.select_related().filter(director_id=person_id)
    personrewards = PersonReward.objects.select_related().filter(for_person_id=person_id)
    comments = CommentPerson.objects.filter(for_person_id=person_id)
    form = CommentPersonForm()

    context = {
        'person': person,
        'movies': movies,
        'director': director,
        'personrewards': personrewards,
        'comments': comments,
        'form': form,
    }

    return render(request, "person.html", context)


def add_comment(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    user = request.user
    form = CommentPersonForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']

        komentarz = CommentPerson()
        komentarz.user = user
        komentarz.for_person = person
        komentarz.text = text
        komentarz.save()

        return HttpResponseRedirect(reverse('Persons.views.person', args=[person_id]))

    return render(request, "person.html", {'person': person, 'form': form})
