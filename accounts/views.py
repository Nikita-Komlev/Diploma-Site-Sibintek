from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def register_view(request):
    if request.user.is_authenticated:
        return redirect('inbox')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна. Пожалуйста, войдите.')
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('inbox')
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inbox')
        else:
            messages.error(request, 'Неправильное ФИО или пароль.')
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class ProfileListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'userprofiles'

    def get_queryset(self):
        # Filter the queryset to include only the current user's profile
        return CustomUser.objects.filter(id=self.request.user.id)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'userprofile'
    pk_url_kwarg = 'user_id'  # URL parameter name for the user's ID

    def get_queryset(self):
        # Return the queryset of CustomUser objects
        return CustomUser.objects.all()