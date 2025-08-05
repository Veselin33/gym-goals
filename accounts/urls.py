from django.urls import path
from accounts import views
from accounts.views import UserRegisterView, EditProfileDetails, CustomLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/profile-edit/', EditProfileDetails.as_view(), name='profile-edit'),
    path('profile/details-info/', views.profile_information, name='profile-detail'),
]
