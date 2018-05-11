from django.forms import ModelForm
from .models import Albums, Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        self.fields['image'].queryset = Photo.objects.filter(
                                        user__username=username)


class AlbumsForm(ModelForm):
    class Meta:
        model = Albums
        fields = ['cover', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        self.fields['cover'].queryset = Photo.objects.filter(
                                        user__username=username)
