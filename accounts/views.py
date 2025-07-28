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
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')



def logout_view(request):
    logout(request)
    return redirect('login')


class ProfileDetails(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile-details.html'
    success_url = reverse_lazy('profile-info')

    def get_object(self, queryset=None):
        return self.request.user.profile


def profile_information(request):
    profile = request.user.profile
    bmi = profile.bmi

    return render(request, 'profile-update.html', {'profile': profile, 'bmi': bmi})

