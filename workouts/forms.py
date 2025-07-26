from django import forms
from django.views.generic import TemplateView

from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type', 'duration_minutes']
        widgets = {
            'workout_type': forms.Select(attrs={'class': 'form-control'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class WorkoutSuccessView(TemplateView):
    template_name = 'workout-success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout'] = self.request.session.get('last_workout_data', {})
        return context
