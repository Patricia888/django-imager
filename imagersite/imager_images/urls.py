from django.urls import path
from .views import (
    LibraryView, AlbumsViewDetail,
    PhotoViewDetail, AlbumsView,
    PhotoView, PhotoCreateView,
    AlbumsCreateView, PhotoEditView, AlbumsEditView
)

urlpatterns = [
    path("library", LibraryView.as_view(), name="library"),
    path("albums", AlbumsView.as_view(), name="albums"),
    path("photo", PhotoView.as_view(), name="photo"),
    path("albums/<int:pk>", AlbumsViewDetail.as_view(), name="albums_view_detail"),
    path("photo/<int:pk>", PhotoViewDetail.as_view(), name="photo_view_detail"),
    path("photo/add", PhotoCreateView.as_view(), name="photo_create"),
    path("albums/add", AlbumsCreateView.as_view(), name="albums_create"),
    path("photo/<int:pk>/edit/", PhotoEditView.as_view(), name="photo_edit"),
    path("albums/<int:pk>/edit/", AlbumsEditView.as_view(), name="albums_edit"),
]
