from django.contrib import admin

# Register your models here.
from Persons.models import Person, Actor, Director, CommentPerson


class AdminPerson(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


class AdminActor(admin.ModelAdmin):
    list_display = ('actor', 'character', 'in_movie')
    list_filter = ('actor', 'in_movie')


class AdminDirector(admin.ModelAdmin):
    list_display = ('director', 'in_movie')
    list_filter = ('director', 'in_movie')


class AdminCommentPerson(admin.ModelAdmin):
    list_display = ('for_person',)

admin.site.register(Person, AdminPerson)
admin.site.register(Actor, AdminActor)
admin.site.register(Director, AdminDirector)
admin.site.register(CommentPerson, AdminCommentPerson)

