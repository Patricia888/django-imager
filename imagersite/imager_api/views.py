from rest_freamework import generics
from .serializers import PhotoSerializer
from imager_images.models import Photo, Albums


class PhotoListApi(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)
