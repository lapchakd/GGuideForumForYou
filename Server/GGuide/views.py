from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import ModelFormMixin

from GGuide.models import SignUpForm


def index(request):
    ctx = {

    }
    return render(request, 'index.html', context=ctx)


def registration(request):
    success_url = "/"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(success_url)
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def logout(request, next_page='index'):

    return redirect(next_page)
