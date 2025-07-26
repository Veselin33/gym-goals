from decimal import Decimal
from django.db import models

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Stretching', 'Stretching'),
        ('HIIT', 'HIIT'),
        ('Other', 'Other'),
    ]

    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()

    def calculate_calories(self, user_weight_kg):
        met_values = {
            'Cardio': 8.0,
            'Strength': 6.0,
            'Stretching': 3.0,
            'HIIT': 9.5,
            'Other': 5.0,
        }
        met = met_values.get(self.workout_type, 5.0)

        weight = float(user_weight_kg) if isinstance(user_weight_kg, Decimal) else user_weight_kg

        calories = met * weight * (self.duration_minutes / 60)
        return round(calories)