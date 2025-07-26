from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser, Profile
from accounts.validators import validate_username


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter a valid Email'}),
        }

    username = forms.CharField(
        max_length=30,
        validators=[
            validate_username
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Username can contain only letters and digits'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = None


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'weight_kg': forms.NumberInput(attrs={'placeholder': 'Enter your weight in kg'}),
            'height_cm': forms.NumberInput(attrs={'placeholder': 'Enter your height in cm'}),
            'target_weight_kg': forms.NumberInput(attrs={'placeholder': 'Enter your target weight in kg'}),
            'profile_image': forms.FileInput(),
        }

