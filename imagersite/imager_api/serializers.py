from rest_framework import serializers
from imager_images.models import Photo, Albums


class PhotoSerializer(serializers.ModelSerializer):
    """Converts data into json text."""
    class Meta:
        model = Photo
        fields = (
            'user', 'image', 'title', 'description', 'date_uploaded',
            'date_modified', 'date_published', 'published'
        )
