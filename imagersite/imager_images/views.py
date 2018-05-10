from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
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

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Albums.objects.filter(id=self.kwargs['id'].first())


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
    # pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(id=self.kwargs['pk'])


# class AlbumsAddView(CreateView):
#     """  """
#     template_name = 'imager_profile/albums_add.html'
#     model = Albums

#     def get(self, *args, **kwargs):

#     def post(self, *args, **kwargs):

#     def get_form_kwargs(self):


# class PhotoAddView(CreateView):
#     """  """
#     template_name = 'imager_profile/photo_add.html'
#     model = Photo

#     def get(self, *args, **kwargs):
#         if not self.request.user.is_authenticated:
#             return redirect('home')

#         return super().get(*args, **kwargs)

#     def post(self, *args, **kwargs):
#         if not self.request.user.is_authenticated:
#             return redirect('home')

#         return super().get(*args, **kwargs)

#     def get_form_kwargs(self):
