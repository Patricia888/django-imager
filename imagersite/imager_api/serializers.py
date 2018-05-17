from rest_framework import serializers
from imager_images.models import Photo, Albums
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Converts data into json text."""
    user = serializers.HyperlinkIdentityField(
        view_name='user-detail',
        lookup_url_kwarg='username'
    )

    class Meta:
        model = Photo
        fields = (
            'user', 'image', 'title', 'description', 'date_uploaded',
            'date_modified', 'date_published', 'published'
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email',
            'password', 'first_name', 'last_name'
        )

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email']
        })

        user.set_password(validated_data['password'])
        user.save()
        return user
