from django.urls import path
from accounts import views
from accounts.views import UserRegisterView, ProfileDetails, CustomLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/body-metrics', ProfileDetails.as_view(), name='body-metrics'),
    path('profile/info/', views.profile_information, name='profile-info'),
]
