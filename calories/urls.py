from django.urls import path

from calories import views

urlpatterns = [
    path('calculator/', views.calories_view, name='calories'),
    path('result/', views.calories_result_view, name='calories_result'),

]