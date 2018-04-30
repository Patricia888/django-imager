from django.urls import path
from .views import library_view, albums_view_detail, photo_view_detail, albums_view, photo_view

urlpatterns = [
    path("images/library", library_view, name="library"),
    path("albums/", albums_view, name="albums"),
    path("photo/", photo_view, name="photo"),
    path("images/albums/<int:albums_id>", albums_view_detail, name="albums"),
    path("images/photo/<int:photo_id>", photo_view_detail, name="photo"),
]
