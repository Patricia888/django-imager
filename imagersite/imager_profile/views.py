from django.contrib.auth.mixins import LoginRequiredMixin
from imager_images.models import Albums, Photo
from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import ProfileEditForm
from .models import ImagerProfile
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


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Lets the user edit their profile."""
    template_name = 'imager_profile/profile_edit.html'
    model = ImagerProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('profile')
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)
