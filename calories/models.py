from django.db import models
from django.db.models import ForeignKey
from accounts.models import CustomUser


# Create your models here.

class Calories(models.Model):
    ACTIVITY_CHOICES = (
        ('Sedentary', 'Sedentary'),
        ('Light', 'Light'),
        ('Moderate', 'Moderate'),
        ('Active', 'Active'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


    user = ForeignKey(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1 ,choices=GENDER_CHOICES)
    activity = models.CharField(max_length=20 ,choices=ACTIVITY_CHOICES)
    calories = models.FloatField()




