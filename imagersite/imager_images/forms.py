from django.forms import ModelForm
from .models import Albums, Photo


class PhotoForm(ModelForm):
    """Lets the user add photos to their collection."""
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        self.fields['image'].queryset = Photo.objects.filter(
                                        user__username=username)


class AlbumsForm(ModelForm):
    """Lets the user add albums to their collection."""
    class Meta:
        model = Albums
        fields = ['cover', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        self.fields['cover'].queryset = Photo.objects.filter(
                                        user__username=username)


class PhotoEditForm(ModelForm):
    """Lets the user edit photo information."""
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        username = kwargs.pop('username')

        self.fields['image'].queryset = Photo.objects.filter(
                                        album__user__username=username)


class AlbumsEditForm(ModelForm):
    """Lets the user edit an album."""
    class Meta:
        model = Albums
        fields = ['cover', 'title', 'description', 'published']

        def __init__(self, *args, **kwargs):
            username = kwargs.pop('username')
            super().__init__(*args, **kwargs)
            self.fields['cover'].queryset = Photo.objects.filter(
                album__user__username=username)

