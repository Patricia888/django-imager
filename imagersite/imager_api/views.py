from rest_framework.authentication import TokenAuthentication
from .serializers import PhotoSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import IsAuthenticated
from rest_framework import generics, status
from imager_images.models import Photo


class PhotoListApi(generics.ListAPIView):
    """Returns a JSON file that contains information about the current user."""
    permission_classes = (IsAuthenticated, )
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)


class UserApi(generics.RetrieveAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializers_class = UserSerializer

    def retrieve(self, request, pk=None):
        if not pk:
            return Response(
                UserSerializer(request.user).data,
                status=status.HTTP_200_OK
            )
        return super().retrieve(request, pk)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valids:
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
