from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """ test creating a new user with email """
        email = "shiro@gg.com"
        password = "666"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Teste email for a new user is normalized"""

        email = "shor@SHIROLOCO.COM"

        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'balala')

    def test_create_new_superuser(self):
        """Teste creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'shiro@shiro.com',
            'doggito'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
