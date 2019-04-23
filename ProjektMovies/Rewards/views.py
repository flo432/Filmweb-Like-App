from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Reward, MovieReward, PersonReward


# Create your views here.


def rewards(request):
    rewards = Reward.objects.order_by('name')
    paginator = Paginator(rewards, 10)

    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        "rewards": rewards,
        'object_list': page,
    }

    return render(request, "rewards.html", context)


def reward(request, reward_name):
    reward = get_object_or_404(Reward, name=reward_name)
    relatedmovies = MovieReward.objects.select_related().filter(reward_id=reward.id)
    relatedpersons = PersonReward.objects.select_related().filter(reward_id=reward.id)

    context = {
        'reward': reward,
        'relatedmovies': relatedmovies,
        'relatedpersons': relatedpersons,
    }

    return render(request, "reward.html", context)
