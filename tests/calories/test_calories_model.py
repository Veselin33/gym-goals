from django.core.exceptions import ValidationError

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from calories.models import Calories


class TestCaloriesModel(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email = "test@test.com",
            password = "12pass34",
        )

    def test__required_age_field__is_empty(self):
        calorie = Calories(
            user = self.user,
            age = None,
            gender = 'M',
            activity='BMR',
            calories = 2500.00
        )
        with self.assertRaises(ValidationError):
            calorie.full_clean()

    def test__required_gender_field__is_empty(self):
        calorie = Calories(
            user = self.user,
            age = 27,
            activity='BMR',
            gender = '',
            calories = 2500.00
        )
        with self.assertRaises(ValidationError):
            calorie.full_clean()


    def test__required_activity_field__is_empty(self):
        calorie = Calories(
            user = self.user,
            gender = 'M',
            age = 27,
            calories = 2500.00,
            activity = ''
        )
        with self.assertRaises(ValidationError):
            calorie.full_clean()

class TestUserCaloriesCalculationFlow(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email = "test@test.com",
            password = "12pass34",
        )
        self.profile = self.user.profile
        self.profile.height_cm = 180
        self.profile.weight_kg = 80
        self.profile.save()

    def test__calculation_flow__for__logged_in_user(self):
        self.client.login(username = "testuser", password = "12pass34")
        response = self.client.post(reverse('calories'), {
            'age': 27,
            'gender': 'M',
            'activity': 'BMR',
        })


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('calories_result'))
        result = Calories.objects.first()
        self.assertEqual(result.age, 27)
        self.assertEqual(result.gender, 'M')
        self.assertEqual(result.activity, 'BMR')
        self.assertEqual(result.user, self.user)

