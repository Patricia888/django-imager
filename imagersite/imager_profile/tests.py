from django.test import TestCase
from .models import ImagerProfile, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerProfile

    phone = factory.Faker('phone_number')
    location = factory.Faker('street_address')
    website = factory.Faker('uri')
    fee = 45
    camera = 'dsr'


class ProfileUnitTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)



    # code review examples
    # inside profile unit tests

    # the tests below don't work with setUp and tearDown


    # def test_get_home_page(self):
    #     '''test home page'''
    #     response = self.client.get(reverse_lazy('home'), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.templates[0].name, 'generic/home.html')
    #     self.assertEqual(response.templates[1].name, 'generic/base.html')

    # def test_get_registration_page(self):
    #     '''test registration page'''
    #     response = self.client.get(reverse_lazy('registration_register'), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.templates[0].name, 'registration/registration_form.html')
    #     self.assertEqual(response.templates[1].name, 'generic/base.html')

    # def test_register_user(self):
    #     '''test user registration'''
    #     response = self.client.post(reverse_lazy('registration_register'), {'username': 'wat', 'password1': 'password', 'password2': 'password', 'email': 'wat@wat.com', follow=True})
    #     self.assertEqual(respone.status_code, 200)
    #     self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')
    #     self.assertEqual(response.templates[1].name, 'generic/base.html')
    #     self.assertEqual(len(mail.outbox), 1)
    #     email = mail.outbox[0]
    #     self.assertEqual(email.to, ['wat@wat.com'])
    #     register_url = email.body.splitlines()[-1]
    #     # takes a url, splits in to pieces, gives back a url dictionary
    #     # includes host, port, path, any ids.....
    #     # lets you test pieces instead of whole url
    #     # client object only takes path. Parsing lets you access that.
    #     register_url = urlparse(register_url)
    #     response = self.client.get(register_url.path)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(self.client.login(username='wat', password='password'))
