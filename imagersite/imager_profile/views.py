from django.shortcuts import redirect, render, get_object_or_404
from imager_images.models import Albums, Photo
from .models import ImagerProfile
from django.views.generic import DetailView
from django.conf import settings


# def profile_view(request, username=None):
#     '''Shows profile.'''
#     owner = False

#     if not username:
#         username = request.user.get_username()
#         owner = True
#         if username == "":
#             return redirect("home")

#     profile = get_object_or_404(ImagerProfile, user__username=username)
#     albums = Albums.objects.filter(user__username=username)
#     photos = Photo.objects.filter(albums__user__username=username)

#     if not owner:
#         photos = Photo.objects.filter(published="PUBLIC")
#         albums = Albums.objects.filter(published="PUBLIC")

#     context = {
#         "profile": profile,
#         "albums": albums,
#         "photos": photos,
#     }

#     return render(request, "imager_profile/profile.html", context)


def settings_view(request, username=None):
    '''Show the user settings.'''
    pass


# profile class
class ProfileView(DetailView):
    template_name = 'imager_profile/profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'
    model = ImagerProfile
    context_object_name = 'profile'


    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        # import pdb; pdb.set_trace()
        if kwargs:
            return super().get(*args, **kwargs)

        else:
            self.kwargs.update({'username': self.request.user.username})
            # kwargs.update({'owner': True})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import pdb; pdb.set_trace()

        # profile = get_object_or_404(ImagerProfile, user__username=kwargs['username'])
        albums = Albums.objects.filter(user__username=self.request.user.username)
        photos = Photo.objects.filter(user__username=self.request.user.username)
        # number_of_photos = photos.count()
        # number_of_albums = albums.count()

        if context['profile'].user.username != self.request.user.username:
            photos = photos.filter(published='PUBLIC')
            albums = albums.filter(published='PUBLIC')

        # context['profile'] = profile
        context['pub_albums'] = albums
        context['pub_photos'] = photos
        context['priv_albums'] = albums.filter(published='PRIVATE')
        context['priv_photos'] = photos.filter(published='PRIVATE')
        # context['number_of_photos'] = number_of_photos
        # context['number_of_albums'] = number_of_albums

        return context
