from django.urls import path

from workouts.forms import WorkoutSuccessView
from workouts.views import WorkoutCreateView

urlpatterns = [
    path('add-workout', WorkoutCreateView.as_view(), name='add_workout'),
    path('workout-success/', WorkoutSuccessView.as_view(), name='workout_success'),
]