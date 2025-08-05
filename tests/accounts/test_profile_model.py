from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import Profile, CustomUser


class TestProfileModel(TestCase):
    def test__profile_created__on_user_creation(self):
        user = CustomUser.objects.create_user(
            username='TestUsername',
            email='test@test.com',
            password='12pass34',
        )

        self.assertTrue(hasattr(user, 'profile'))
        self.assertIsInstance(user.profile, Profile)

    def test__profile__bmi(self):
        user = CustomUser.objects.create_user(
            username='TestUsername',
            email='test@test.com',
            password='12pass34',
        )

        profile = user.profile

        profile.weight_kg = 70
        profile.height_cm = 170

        expected_bmi = round(70 / (1.70 ** 2), 2)
        self.assertEqual(profile.bmi(), expected_bmi)

    def test__profile__bmi__no_height_and_weight(self):
        user = CustomUser.objects.create_user(
            username='TestUsername',
            email='test@test.com',
            password='12pass34',
        )

        profile = user.profile

        self.assertEqual(profile.bmi(), '(BMI) requires Height And Weight.')

    def test__profile__min_height__raises__MinValueError(self):
        user = CustomUser.objects.create_user(
            username='TestUsername',
            email='test@test.com',
            password='12pass34',
        )
        profile = user.profile

        profile.height_cm = 100

        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test__profile__min_weight__raises__MinValueError(self):
        user = CustomUser.objects.create_user(
            username='TestUsername',
            email='test@test.com',
            password='12pass34',
        )

        profile = user.profile
        profile.weight_kg = 29
        with self.assertRaises(ValidationError):
            profile.full_clean()