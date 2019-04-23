from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Genres.models import Genre, MovieGenre


def genres(request):

    genres = Genre.objects.all()
    paginator = Paginator(genres, 5)

    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        "genres": genres,
        'object_list': page,
    }

    return render(request, "genres.html", context)


def genre(request, genre_name):

    genre = get_object_or_404(Genre, name=genre_name)

    relatedmovies = MovieGenre.objects.select_related().filter(genre_id=genre.id)

    context = {
        'genre': genre,
        'relatedmovies': relatedmovies,

    }

    return render(request, "genre.html", context)
