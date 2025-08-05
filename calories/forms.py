from django import forms

from calories.models import Calories


class CaloriesForm(forms.ModelForm):
    class Meta:
        model = Calories
        exclude = ('user', 'calories')

