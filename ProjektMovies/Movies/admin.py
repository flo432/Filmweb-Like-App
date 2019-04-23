from django.contrib import admin

# Register your models here.
from Movies.models import Movie, CommentMovie, RateMovie


class AdminMovie(admin.ModelAdmin):
    list_display = ('title', 'relase_date')
    list_filter = ('title', 'relase_date')


class AdminCommentMovie(admin.ModelAdmin):
    list_display = ('for_movie',)


class AdminRateMovie(admin.ModelAdmin):
    list_display = ('rate', 'user', 'for_movie')

admin.site.register(Movie, AdminMovie)
admin.site.register(CommentMovie, AdminCommentMovie)
admin.site.register(RateMovie, AdminRateMovie)
