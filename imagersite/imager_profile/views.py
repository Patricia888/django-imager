from django.shortcuts import redirect, render, get_object_or_404
from imager_images.models import Albums, Photo
from .models import ImagerProfile


def profile_view(request, username=None):
    '''Shows profile.'''
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(albums__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos,
    }

    return render(request, "imager_profile/profile.html", context)


def settings_view(request, username=None):
    '''Show the user settings.'''
    pass


