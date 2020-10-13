from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "admim@gamil.com"
        password = "123admin123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        return self.assertEqual(user.email, email) and self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "admin@gmail.com"
        password = "123admim123"
        user = get_user_model().objects.create_user(email=email, password=password)
        return self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # temp = get_user_model().objects.create_user(None, "123admin123").len
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "123admin123")
        # if temp == 0:
        #     return self.assertRaises(ValueError)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'admin"gmail.com',
            '123admin123'
        )
        return user.is_superuser and user.is_staff
