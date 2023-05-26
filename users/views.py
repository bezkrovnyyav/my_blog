from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomRegisterForm, CustomProfileUpdateForm, CustomUpdateForm
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username} Please Login ')
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = CustomUpdateForm(request.POST, instance=request.user)
        profile_form = CustomProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account is updated!')
            return redirect('profile')

    else:
        user_form = CustomUpdateForm(instance=request.user)
        profile_form = CustomProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, 'users/profile_update.html', context)
