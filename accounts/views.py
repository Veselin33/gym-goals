from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import CustomUserCreationForm, ProfileForm
from accounts.forms import LoginForm
from accounts.models import CustomUser, Profile


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')



def logout_view(request):
    logout(request)
    return redirect('login')


class EditProfileDetails(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self, queryset=None):
        return self.request.user.profile


def profile_information(request):
    user_profile = request.user.profile
    bmi = user_profile.bmi

    return render(request, 'profiles/profile-detail.html', {'user_profile': user_profile, 'bmi': bmi})
