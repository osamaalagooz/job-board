from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm, UserForm
from django.contrib.auth import authenticate, login
from .models import Profile


# Create your views here.
def sign_up(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           login(request, user)
           return redirect('/accounts/profile')
           
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)

def profile(request):

    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

def edit_profile(request):
    
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profileform = ProfileForm(request.POST,request.FILES, instance=profile)
        userform = UserForm(request.POST, instance=request.user )
        if profileform.is_valid() and userform.is_valid():
           userform.save()
           my_profileform = profileform.save(commit=False) 
           my_profileform.user = request.user
           my_profileform.save()
           return redirect('/accounts/profile')
           
    else:
        profileform = ProfileForm(instance=profile)
        userform = UserForm(instance=request.user)

    context = {
        'profileform': profileform ,
        'userform': userform,
    }
    return render(request, 'accounts/profile_edit.html', context)