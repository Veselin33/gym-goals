from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Profile


# Create your views here.

def base_view(request):
    return render(request, 'common/home.html')


def bmi_view(request):
        user_profile = None
        bmi = None

        if request.user.is_authenticated:
            user_profile = request.user.profile
            bmi = user_profile.bmi()

        return render(request, 'common/bmi-calculator.html', {
            'user_profile': user_profile,
            'bmi': bmi
        })
