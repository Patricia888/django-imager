from django.shortcuts import redirect, render, get_object_or_404
from imager_images.models import Albums, Photo


def library_view(request):
    '''Will show the user\'s library.'''
  
    username = request.user.get_username()
    if username == "":
        return redirect("home")

    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    context = {
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

    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
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

    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
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

    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
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

    albums = Albums.objects.filter(user__username=username)
    photos = Photo.objects.filter(product__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published="PUBLIC")
        albums = Albums.objects.filter(published="PUBLIC")

    context = {
        "albums": albums,
        "photos": photos
    }

    return render(request, "imager_profile/photo.html", context)

