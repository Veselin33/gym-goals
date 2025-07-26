from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request, 'home.html')

def bmi_view(request):
    return render(request, 'bmi-calculator.html')
