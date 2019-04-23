from django.shortcuts import render


def profile(request):

    user = request.user

    context = {
        "user": user,
    }

    return render(request, "profile.html", context)
