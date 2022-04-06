from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normaluser@mail.com", password="foo")
        self.assertEqual(user.email, "normaluser@mail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(str(user), user.email)

        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email="superuser@mail.com", password="foo")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="superuser@mail.com", password="foo", is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="superuser@mail.com", password="foo", is_superuser=False)
