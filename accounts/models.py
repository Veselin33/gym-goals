from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GOAL_CHOICES = [
        ('cut', 'Cut (Lose Weight)'),
        ('gain', 'Gain Weight'),
        ('maintain', 'Maintain Weight'),
    ]

    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, null=True, blank=True)
    target_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def bmi(self):
        if self.height_cm and self.weight_kg:
            height_m = self.height_cm / 100
            return round(float(self.weight_kg) / (height_m ** 2), 2)
        return None

    def __str__(self):
        return self.username
