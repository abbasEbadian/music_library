from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('app_music:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'accounts/profile.html')
