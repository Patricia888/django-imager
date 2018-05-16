from rest_framework import generics
from .serializers import PhotoSerializer
from imager_images.models import Photo, Albums


class PhotoListApi(generics.ListAPIView):
    """Returns a JSON file that contains information about the current user."""
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)
