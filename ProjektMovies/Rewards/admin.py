from django.contrib import admin
from Rewards.models import Reward, MovieReward, PersonReward
# Register your models here.


class AdminReward(admin.ModelAdmin):
    list_display = ('name',)


class AdminMovieReward(admin.ModelAdmin):
    list_display = ('reward', 'for_movie')


class AdminPersonReward(admin.ModelAdmin):
    list_display = ('reward', 'for_person')


admin.site.register(Reward, AdminReward)
admin.site.register(MovieReward, AdminMovieReward)
admin.site.register(PersonReward, AdminPersonReward)
