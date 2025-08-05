from django.contrib import admin
from .models import Calories

# Register your models here.

@admin.register(Calories)
class CaloriesAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'activity', 'calories')
    list_filter = ('gender', 'activity')
    search_fields = ('user__username',)
