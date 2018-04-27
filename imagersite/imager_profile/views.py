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
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/profile.html", context)


def settings_view(request, username=None):
    '''Show the user settings.'''
    pass


def library_view(request, username=None):
    '''Will show the user\'s library.'''
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/library.html", context)


def albums_view_detail(request, username=None):
    '''shows one album'''
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

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
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/albums.html", context)


def photo_view_detail(request, username=None):
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

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
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == "":
            return redirect("home")

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "profile": profile,
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/photo.html", context)

