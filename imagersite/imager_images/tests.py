from django.test import TestCase
from .models import User
import factory

from .models import Albums, Photo
# from imager_profile.models import ImagerProfile
from random import choice
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os


class UserFactory(factory.django.DjangoModelFactory):
    '''testing user'''
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class PhotoFactory(factory.django.DjangoModelFactory):
    """testing photo"""
    class Meta:
        model = Photo
    # user = factory.Faker('name')
    image = SimpleUploadedFile(
        name='image.jpg',
        content=open(
            os.path.join(settings.BASE_DIR, 'imagersite/static/flowers.jpg'), 'rb'
        ).read(),
        content_type="image/jpeg"
    )
    title = factory.Faker('name')
    description = factory.Faker('name')
    date_uploaded = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    published = choice(['private', 'shared', 'public'])


class AlbumsFactory(factory.django.DjangoModelFactory):
    """testing albums"""
    class Meta:
        model = Albums

    title = factory.Faker('name')
    description = factory.Faker('sentence')
    date_created = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    published = choice(['private', 'shared', 'public'])


class ProfileUnitTests(TestCase):
    """testing photo and albums"""
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()
            # profile = ProfileFactory.create(user=user)
            # profile.save()
            photo = PhotoFactory.create(user=user)
            photo.save()
            albums = AlbumsFactory.create(user=user)
            albums.save()

    @classmethod
    def tearDownClass(cls):
        '''tear down fake database'''
        super(TestCase, cls)
        User.objects.all().delete()

    def test_one_photo(self):
        """test photo is there when it is there"""
        one_photo = Photo.objects.first()
        self.assertIsNotNone(one_photo)

    def test_photo_title(self):
        """test photo that the photo title is a str"""
        image = Photo.objects.first()
        self.assertIsInstance(image.title, str)

    # def test_photo_description(self):
    #     """test that the photo description is a str"""
    #     image = Photo.objects.first()
    #     self.assertIsInstance(image.description, str)

    def test_photo_date_uploaded(self):
        """test photo upload date"""
        image = Photo.objects.first()
        self.assertIsInstance(image.date_uploaded, object)

    def test_one_albums(self):
        """test albums is there when it is there"""
        one_albums = Albums.objects.first()
        self.assertIsNotNone(one_albums)

    def test_albums_title(self):
        """test that the albums title is a str"""
        albums = Albums.objects.first()
        self.assertIsInstance(albums.title, str)

    def test_albums_description(self):
        """test that the albums description is a str"""
        albums = Albums.objects.first()
        self.assertIsInstance(albums.description, str)
