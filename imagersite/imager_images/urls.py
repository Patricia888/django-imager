from django.urls import path
from .views import (
    LibraryView, albums_view_detail,
    photo_view_detail, albums_view,
    PhotoView
)

urlpatterns = [
    path("library", LibraryView.as_view(), name="library"),
    path("albums", albums_view, name="albums"),
    path("photo", PhotoView.as_view(), name="photo"),
    path("albums/<int:albums_id>", albums_view_detail, name="albums"),
    path("photo/<int:photo_id>", photo_view_detail, name="photo"),
]
