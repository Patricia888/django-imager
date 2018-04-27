from django.urls import path
from .views import profile_view, settings_view

urlpatterns = [
    path("", profile_view, name="profile"),
    path("<str:username>/", profile_view, name="named_profile"),
    path("settings/<str:username>", settings_view, name="settings"),
]
