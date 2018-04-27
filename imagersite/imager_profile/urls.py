from django.urls import path
from .views import profile_view, settings_view, library_view, albums_view, photo_view

urlpatterns = [
    path("", profile_view, name="profile"),
    path("<str:username>/", profile_view, name="named_profile"),
    path("settings/<str:username>", settings_view, name="settings"),
    path("images/library", library_view, name="library"),
    path("images/albums/<str:albums_id>", albums_view, name="albums"),
    path("images/photo/<str:photo_id>", photo_view, name="photo"),
]
