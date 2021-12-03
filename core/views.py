from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from . import forms
from . import models


# Create your views here.


def home(request):
    movies = models.MovieList.objects.filter()
    context = {'movies': movies}

    return render(request, 'core/base.html', context)


def loginpage(request):
    page = 'login_page'
    rq = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Username or password does not exist')
        if rq == 'http://localhost:8000/login/?next=/upload/':
            return redirect('upload_page')
        else:
            return redirect('home')

    context = {'page': page}

    return render(request, 'core/login_page.html', context)


@login_required(login_url='login_page')
def uploadpage(request):
    form = forms.AddMovie()
    if request.method == 'POST':
        form = forms.AddMovie(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'core/upload_page.html', context)


def registerpage(request):
    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error ocurred during registration.')

    context = {'form': form}

    return render(request, 'core/register_page.html', context)


def userlogout(request):
    logout(request)
    return redirect('home')
