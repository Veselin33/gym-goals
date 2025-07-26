from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Workout
from .forms import WorkoutForm

class WorkoutCreateView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'add-workout.html'



    def form_valid(self, form):
        profile = self.request.user.profile
        user_weight = profile.weight_kg or 70
        self.object = form.save(commit=False)
        calories_burned = self.object.calculate_calories(user_weight)
        self.object.save()


        self.request.session['last_workout_data'] = {
            'workout_type': self.object.workout_type,
            'duration': self.object.duration_minutes,
            'calories': calories_burned,
        }

        return redirect('workout_success')
