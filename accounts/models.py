from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.validators import min_weight_validator, min_height_validator


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)




class Profile(models.Model):
    GOAL_CHOICES = [
        ('cut', 'Cut (Lose Weight)'),
        ('gain', 'Gain Weight'),
        ('maintain', 'Maintain Weight'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, validators=[min_weight_validator], blank=True, null=True)
    height_cm = models.PositiveIntegerField(validators=[min_height_validator], blank=True, null=True)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, null=True, blank=True)
    target_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def bmi(self):
        if self.height_cm and self.weight_kg:
            height_m = self.height_cm / 100
            return round(float(self.weight_kg) / (height_m ** 2), 2)
        return '(BMI) requires Height And Weight.'

    def __str__(self):
        return self.user.username
