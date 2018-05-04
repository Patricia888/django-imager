from django.shortcuts import redirect, render, get_object_or_404
from imager_images.models import Albums, Photo
from imager_profile.models import ImagerProfile


def library_view(request, username=None):
    '''Will show the user\'s library.'''

    if not username: # pragma: no cover
        username = request.user.get_username()
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(albums__user__username=username)

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos,
    }

    return render(request, "imager_profile/library.html", context)


def albums_view_detail(request, username=None):
    '''shows one album'''
    owner = False # pragma: no cover

    if not username: # pragma: no cover
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
        "photos": photos
    }

    return render(request, "imager_profile/albums.html", context)


def albums_view(request, username=None):
    '''shows all albums'''
    if not username: # pragma: no cover
        username = request.user.get_username()
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(albums__user__username=username)

    photos = Photo.objects.filter(published="PUBLIC")
    albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/albums.html", context)


def photo_view_detail(request, username=None):
    owner = False # pragma: no cover

    if not username: # pragma: no cover
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
        "photos": photos
    }

    return render(request, "imager_profile/photo.html", context)


def photo_view(request, username=None):
    if not username: # pragma: no cover
        username = request.user.get_username()
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(albums__user__username=username)

    photos = Photo.objects.filter(published="PUBLIC")
    albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/photo.html", context)
