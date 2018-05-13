from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from imager_images.models import Albums, Photo
from imager_profile.models import ImagerProfile
from .forms import PhotoForm, AlbumsForm
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


class AlbumsViewDetail(DetailView):
    """Displays detail on an album from users account."""
    template_name = 'imager_profile/albums_view_detail.html'
    context_object_name = 'albums'
    pk_url_kwargs = 'id'
    model = Albums

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


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


class PhotoViewDetail(DetailView):
    """Displays detail on a photo from users account."""
    template_name = 'imager_profile/photo_view_detail.html'
    context_object_name = 'photo'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(id=self.kwargs['pk'])


class PhotoCreateView(LoginRequiredMixin, CreateView):
    """Lets a uer add a photo."""
    template_name = 'imager_profile/photo_add.html'
    login_url = reverse_lazy('auth_login')
    form_class = PhotoForm
    success_url = reverse_lazy('library')
    model = Photo

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumsCreateView(LoginRequiredMixin, CreateView):
    """Lets a user create an album."""
    template_name = 'imager_profile/albums_add.html'
    login_url = reverse_lazy('auth_login')
    form_class = AlbumsForm
    success_url = reverse_lazy('albums')
    model = Albums

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
