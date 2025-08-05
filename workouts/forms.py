from django import forms


from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type', 'duration_minutes']
        widgets = {
            'workout_type': forms.Select(),
            'duration_minutes': forms.NumberInput(),
        }

