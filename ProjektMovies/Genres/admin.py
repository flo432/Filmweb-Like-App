from django.contrib import admin

# Register your models here.
from Genres.models import MovieGenre, Genre


class AdminGenre(admin.ModelAdmin):
    list_display = ('id', 'name')


class AdminMovieGenre(admin.ModelAdmin):
    list_display = ('id', 'genre', 'for_movie')
    list_filter = ('genre', 'for_movie')


admin.site.register(Genre, AdminGenre)
admin.site.register(MovieGenre, AdminMovieGenre)
