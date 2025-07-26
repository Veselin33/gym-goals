from django.urls import path

from common import views

urlpatterns = [
    path('', views.base_view, name='home'),
    path('bmi/', views.bmi_view, name='bmi'),
]