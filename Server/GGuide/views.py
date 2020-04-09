from django.shortcuts import render, redirect


def index(request):
    ctx = {

    }
    return render(request, 'index.html', context=ctx)


def registration(request):

    ctx = {

    }
    return render(request, 'registration.html', context=ctx)

