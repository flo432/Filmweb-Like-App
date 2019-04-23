from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models.sql.aggregates import Sum, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from Movies.forms import CommentMovieForm, RateMovieForm
from Rewards.models import MovieReward

from .models import Movie, CommentMovie, RateMovie
from Persons.models import Director, Actor
from Genres.models import MovieGenre


# Create your views here.


def movies(request):

    movies = Movie.objects.order_by('title')
    paginator = Paginator(movies, 5)

    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        "movies": movies,
        'object_list': page,
    }

    return render(request, "movies.html", context)


def movie(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)
    moviedirector = Director.objects.select_related().filter(in_movie_id=movie.id)
    movieactors = Actor.objects.select_related().filter(in_movie_id=movie.id)
    moviegenres = MovieGenre.objects.select_related().filter(for_movie_id=movie.id)
    movierewards = MovieReward.objects.select_related().filter(for_movie_id=movie.id)
    comments = CommentMovie.objects.select_related().filter(for_movie_id=movie.id)
    ratings = RateMovie.objects.filter(for_movie_id=movie_id)

    form = CommentMovieForm()
    form2 = RateMovieForm()
    context = {
        'movie': movie,
        'moviedirector': moviedirector,
        'movieactors': movieactors,
        'moviegenres': moviegenres,
        "movierewards": movierewards,
        "comments": comments,
        "ratings": ratings,
        "form": form,
        "form2": form2,
    }

    return render(request, "movie.html", context)


def add_comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    print(movie.id)
    form = CommentMovieForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']

        komentarz = CommentMovie()
        komentarz.user = user
        komentarz.for_movie = movie
        komentarz.text = text
        komentarz.save()

        print(user)
        print(movie.id)
        print(text)

        return HttpResponseRedirect(reverse('Movies.views.movie', args=[movie_id]))

    return render(request, "movie.html", {'movie': movie, 'form': form})


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user =request.user

    form = RateMovieForm(request.POST)

    if form.is_valid():
        rate = form.cleaned_data['rate']

        user_rate = RateMovie()
        user_rate.user = user
        user_rate.for_movie = movie
        user_rate.rate = rate
        user_rate.save()

        return HttpResponseRedirect(reverse('Movies.views.movie', args=[movie_id]))

    return render(request, "movie.html", {'movie': movie, 'form': form})
