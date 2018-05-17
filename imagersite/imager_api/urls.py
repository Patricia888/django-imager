from rest_framework.authtoken import views
from .views import PhotoListApi, UserApi
from django.urls import path


urlpatterns = [
    path('photo/', PhotoListApi.as_view(), name="photo_list_api"),
    path('user/', UserApi.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
]
