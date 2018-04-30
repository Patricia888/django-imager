from django.test import TestCase
from .models import ImagerProfile, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Creates dummy user instance for test cases."""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


# obsolete
# only need to generate Faker info

# obsolete because in the models we are generating an empty profile for each user

# class ProfileFactory(factory.django.DjangoModelFactory):
#     """Creates Profile for users ImagerProfile."""
#     class Meta:
#         model = ImagerProfile

#     phone = factory.Faker('phone_number')
#     location = factory.Faker('street_address')
#     website = factory.Faker('uri')
#     fee = 45
#     bio = 'bio'
#     camera = 'dsr'


class ProfileUnitTests(TestCase):
    """Unit test cases used for testing functionality inside project"""
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            # OBSOLETE (because of stuff in models)
            # profile = ProfileFactory.create(user=user)
            # profile.save()

    @classmethod
    def tearDownClass(cls):
        """Cleans up class by removing all attributes off user."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Tests if user profile is present and active."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_imager_profile_bio(self):
        """testing that the profile bio is a str"""
        prof = ImagerProfile.objects.first()
        self.assertNotIsInstance(prof.bio, str)

    def test_imager_profile_phone(self):
        """testing that the profile phone number is a str"""
        prof = ImagerProfile.objects.first()
        self.assertNotIsInstance(prof.phone, str)

    # def test_profile_view_default_owner_false(self):
    #     '''test that the default is owner is false'''
    #     from .views import profile_view
    #     self.assertFalse(profile_view.owner)



# EXAMPLE from mid term project

# def test_default_behavior_of_about_view(dummy_request):
#     """Test default about behavior."""
#     from ..views.default import about_view
#     response = about_view(dummy_request)
#     assert len(response) == 0
#     assert type(response) == dict