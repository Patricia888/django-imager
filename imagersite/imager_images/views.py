from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from imager_images.models import Albums, Photo
from imager_profile.models import ImagerProfile
from django.conf import settings


class LibraryView(ListView):
    """Displays user's Library view."""
    template_name = 'imager_profile/library.html'
    context_object_name = 'albums'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Albums.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cover'] = settings.STATIC_URL + 'default_cover.thumbnail'

        return context


def albums_view_detail(request, username=None):
    """Displays an album's view."""
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


class AlbumsView(ListView):
    """Displays all albums from users account."""
    template_name = 'imager_profile/albums.html'
    context_object_name = 'albums'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Albums.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class PhotoView(ListView):
    """Displays all images from users account."""
    template_name = 'imager_profile/photo.html'
    context_object_name = 'photo'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
