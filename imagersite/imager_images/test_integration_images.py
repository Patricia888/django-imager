from django.test import TestCase
# from imager_profile.models import User
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Albums, Photo
from model_mommy import mommy
import tempfile
import factory


class TestProfileRoutes(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)

        for n in range(10):
            user = mommy.make(User)
            user.set_password('password')
            user.save()
            product = mommy.make(Albums, user=user)
            mommy.make(
                Photo,
                product=product,
                image=tempfile.NamedTemporaryFile(suffix='.png').name)

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        super(TestCase, cls)

    def test_404_status_on_authenticated_request_to_library(self):
        user = User.objects.first()
        # self.client.login(username=user.username, password='password')
        self.client.force_login(user)
        response = self.client.get('/doesNotExist/')
        self.client.logout()
        self.assertEqual(response.status_code, 404)

    def test_200_status_on_authenticated_request_to_library(self):
        user = User.objects.first()
        # self.client.login(username=user.username, password='password')
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('library'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_albums(self):
        user = User.objects.first()
        # self.client.login(username=user.username, password='password')
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('albums'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_photo(self):
        user = User.objects.first()
        # self.client.login(username=user.username, password='password')
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('photo'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_home(self):
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('home'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_profile(self):
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('profile'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_302_status_on_unauthenticated_request_to_albums(self):
        user = User.objects.first()
        response = self.client.get(reverse_lazy('albums'))
        self.assertEqual(response.status_code, 302)

    def test_only_public_albums_are_shown(self):
        user = User.objects.first()
        albums = Albums.objects.first()
        albums.published = 'PUBLIC'

        albums.save()

        self.client.force_login(user)
        response = self.client.get(reverse_lazy('albums'))
        self.client.logout()

        albums = response.context['albums']
        for als in albums:
            self.assertEqual(als.published, 'PUBLIC')

    def test_only_public_albums_profile_id(self):
        user = User.objects.first()
        albums = Albums.objects.first()
        albums.published = 'PUBLIC'

        albums.save()

        self.client.force_login(user)
        response = self.client.get(reverse_lazy('albums'))
        self.client.logout()

        albums = response.context['profile']
        self.assertEqual(albums.user_id, 1)
   
    def test_only_public_photos_are_shown(self):
        user = User.objects.first()
        photo = Albums.objects.first()
        photo.published = 'PUBLIC'

        photo.save()

        self.client.force_login(user)
        response = self.client.get(reverse_lazy('photo'))
        self.client.logout()

        photos = response.context['photos']
        for als in photos:
            self.assertEqual(als.published, 'PUBLIC')

    def test_only_public_albums_photo_context(self):
        user = User.objects.first()
        albums = Albums.objects.first()
        albums.published = 'PUBLIC'

        albums.save()

        self.client.force_login(user)
        response = self.client.get(reverse_lazy('albums'))
        self.client.logout()

        photos = response.context['photos']
        for als in photos:
            self.assertEqual(als.published, 'PUBLIC')