from django import forms

from calories.models import Calories


class CaloriesForm(forms.ModelForm):
    class Meta:
        model = Calories
        exclude = ('user', 'calories')
        help_texts = {
            'activity': 'Sedentary: little/no exercise, Light: 1–3 days/week, Moderate: 4–5 days/week, Active: daily or intense activity',
        }
