from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.forms import PasswordChangeForm
from GGuide.models import SignUpForm, Userlogin, ProfileForm, ProfileModel


def index(request):
    ctx = {

    }
    return render(request, 'index.html', context=ctx)


def game_views(request):
    return render(request, 'game_index.html', {})


def blog_views(request):
    return render(request, 'blog.html', {})


def registration(request):
    success_url = "/"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            p = ProfileModel(img='default.jpg', user=user)
            p.save()
            return redirect(success_url)
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def logout(request, next_page='index'):

    return redirect(next_page)


def log_in(request):
    success_url = "/"
    if request.method == 'POST':
        form = Userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(success_url)
            else:
                return HttpResponse("Your account was inactive.")
    else:
        form = Userlogin()
    return render(request, 'log_in.html', {})


def profile_user(request):
    ctx = {}
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user  # user
            img = form.cleaned_data.get("Image") # user foto
            user.profilemodel.img = img
            user.profilemodel.save()
            print(user.profilemodel.img) # test
    else:
        form = ProfileForm()
    ctx['form'] = form
    return render(request, 'profile.html', ctx)


def change_info(request):
    ctx ={}
    success_url = "/"
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(success_url)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    ctx['form'] = form
    return render(request, 'change_password.html', ctx)



