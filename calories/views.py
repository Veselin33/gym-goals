from django.shortcuts import render, redirect

from calories.forms import CaloriesForm
from calories.models import Calories


# Create your views here.

def calculate_bmr(age, gender, weight, height, activity):
    if gender == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161


    activity_multipliers = {
        'Sedentary': 1.2,
        'Light': 1.375,
        'Moderate': 1.55,
        'Active': 1.725,
        'Very Active': 1.9,
    }

    tdee = bmr * activity_multipliers.get(activity, 1.2)
    return tdee


def calories_view(request):

    profile = request.user.profile

    try:
        if not profile.weight_kg or not profile.height_cm:
            raise AttributeError
    except AttributeError:
        context = {
            'incomplete_profile': True,
            'metrics_msg': 'You need to give your body metrics (They are required for this feature.)'
        }

        return render(request, 'calories-calculator.html', context)

    if request.method == 'POST':
        form = CaloriesForm(request.POST)
        if form.is_valid():
            calories_obj = form.save(commit=False)
            calories_obj.user = request.user
            calories_obj.calories = calculate_bmr(
                age = calories_obj.age,
                gender = calories_obj.gender,
                weight = float(profile.weight_kg),
                height = float(profile.height_cm),
                activity = calories_obj.activity
            )
            calories_obj.save()

            return redirect('calories_result')
    else:
        form = CaloriesForm()

    return render(request, 'calories-calculator.html', {'form': form})

def calories_result_view(request):
    calories_obj = Calories.objects.filter(user=request.user).last()
    if not calories_obj:
        return redirect('calories')

    return render(request, 'calories-result.html', {'calories_obj': calories_obj})






