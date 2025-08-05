from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from calories.forms import CaloriesForm
from calories.models import Calories


# Create your views here.

def calculate_tdee(age, gender, weight, height, activity):
    if gender == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161


    activity_multipliers = {
        'BMR': 1.0,
        'Sedentary': 1.2,
        'Light': 1.375,
        'Moderate': 1.55,
        'Active': 1.725,
    }

    tdee = bmr * activity_multipliers.get(activity, 1.2)
    return tdee

@login_required
def calories_view(request):
    profile = request.user.profile


    try:
        if not profile.weight_kg or not profile.height_cm:
            raise AttributeError
    except AttributeError:
        context = {
            'incomplete_profile': True,
        }

        return render(request, 'calories/calories-calculator.html', context)

    if request.method == 'POST':
        form = CaloriesForm(request.POST)
        if form.is_valid():
            calories_obj = form.save(commit=False)
            calories_obj.user = request.user
            calories_obj.calories = calculate_tdee(
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

    return render(request, 'calories/calories-calculator.html', {'form': form})


@login_required()
def calories_result_view(request):
    calories_obj = Calories.objects.filter(user=request.user).last()
    if not calories_obj:
        return redirect('calories')

    profile_goal = request.user.profile.goal

    context = {
        'calories_obj': calories_obj,
        'profile_goal': profile_goal,
    }

    return render(request, 'calories/calories-result.html', context)






