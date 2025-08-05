from django.urls import path
from workouts.views import WorkoutCreateView, WorkoutSuccessView

urlpatterns = [
    path('add-workout', WorkoutCreateView.as_view(), name='add_workout'),
    path('workout-success/', WorkoutSuccessView.as_view(), name='workout_success'),
]