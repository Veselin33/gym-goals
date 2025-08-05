from django.contrib import admin
from django.contrib.auth.models import User

from workouts.models import Workout


# Register your models here.

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    model = Workout
    list_display = ('workout_type', 'duration_minutes')
    search_fields = ('workout_type',)