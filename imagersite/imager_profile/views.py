from django.shortcuts import redirect, get_object_or_404
from imager_images.models import Albums, Photo
from .models import ImagerProfile
from django.views.generic import DetailView
from django.conf import settings


def settings_view(request, username=None):
    '''Show the user settings.'''
    pass


class ProfileView(DetailView):
    """ Show user profile. Hides or shows depending on if the user is looking at their own profile or another user's profile. """
    template_name = 'imager_profile/profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'
    model = ImagerProfile
    context_object_name = 'profile'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        if kwargs:
            return super().get(*args, **kwargs)

        else:
            self.kwargs.update({'username': self.request.user.username})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = Albums.objects.filter(user__username=self.request.user.username)
        photos = Photo.objects.filter(user__username=self.request.user.username)

        if context['profile'].user.username != self.request.user.username:
            photos = photos.filter(published='PUBLIC')
            albums = albums.filter(published='PUBLIC')

        context['pub_albums'] = albums
        context['pub_photos'] = photos
        context['priv_albums'] = albums.filter(published='PRIVATE')
        context['priv_photos'] = photos.filter(published='PRIVATE')

        return context
