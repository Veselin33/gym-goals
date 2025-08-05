from django.db import models
from django.db.models import ForeignKey
from accounts.models import CustomUser


# Create your models here.

class Calories(models.Model):
    ACTIVITY_CHOICES = (
        ('BMR', 'BMR (BASE METABOLIC RATE)'),
        ('Sedentary', 'Sedentary: little or no exercise'),
        ('Light', 'Light: exercise 1-3 times/week'),
        ('Moderate', 'Moderate: exercise 4-5 times/week'),
        ('Active', 'Active: exercise 5-7 times/week'),

    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


    user = ForeignKey(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1 ,choices=GENDER_CHOICES)
    activity = models.CharField(max_length=30 ,choices=ACTIVITY_CHOICES)
    calories = models.FloatField()

    def __str__(self):
        return f'{self.user.username} - {self.calories} calories for {self.activity}'




