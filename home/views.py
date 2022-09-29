from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from accounts.models import *
from django.http import HttpResponse, JsonResponse
from accounts.forms import CommentForm
from accounts.models import Game

def homePage(request):
    context = {}
    return render(request, 'frontend/home.html', context)


def registerPage(request):
    context = {}
    form = CreateUserForm()
    forms = UserCountryForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        forms = UserCountryForm(request.POST)

        if all([forms.is_valid(), form.is_valid()]):
            user = form.save()

            if user.id:
                country = forms.save(commit=False)
                country.account = user
                country.save()
                
            group = Group.objects.get(name='User')
            user.groups.add(group)

            forms = UserCountryForm(request.POST)


            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
    context['form'] = form
    context['forms'] = forms
    return render(request, 'frontend/register.html', context)


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'live'))
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'frontend/login.html', context)


@login_required
def logoutPage(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='login')
def livePage(request):
    context = {}
    games = Game.objects.filter(status='ready-to-start')
    context['games'] = games
    return render(request, 'frontend/live.html', context)

@login_required
def news(request):
    context = {}
    games = Game.objects.filter(status='ready-to-start')
    context['games'] = games
    return render(request,'frontend/news.html', context)


def saveComment(request):
    if request.is_ajax:
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return JsonResponse({"error": False}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"hello": "ok"})

def getComment(request):
    comments = Comment.objects.all()
    i = 0
    context = []
    for comment in comments:
        data = {
            'user' : comment.user.username,
            'message' : comment.message,
            'game' : str(comment.game.team1.name + " VS " + comment.game.team2.name),
        }
        context.append(data)
    return JsonResponse({"context": context}, status=200)


@login_required
def video(request):
    context = {}
    games = Game.objects.filter(status='end')
    context['games'] = games
    return render(request,'frontend/video.html', context)