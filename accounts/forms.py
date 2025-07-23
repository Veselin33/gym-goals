from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'weight_kg',
            'height_cm',
            'goal',
            'target_weight_kg',
            'profile_image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

        self.fields['weight_kg'].label = "Weight (kg)"
        self.fields['height_cm'].label = "Height (cm)"
        self.fields['goal'].label = "Fitness Goal"
        self.fields['target_weight_kg'].label = "Target Weight (kg)"
        self.fields['profile_image'].label = "Profile Picture"

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
