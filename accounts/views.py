from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os

from accounts.models import Category, Country
from .forms import *
from .decorators import *


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.groups.all()[0].name == 'Admin':
                return redirect('home')
            else:
                messages.error(request, "Don't be oversmart, you don't have permission")
                logoutCms(request)
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'backend/login/login.html')

def logoutCms(request):
    logout(request)
    return redirect('login-view')

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def home(request):
    context = {}
    return render(request, 'backend/home.html')

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def getCountry(request):
    context = {}
    countries = Country.objects.all().order_by('name')
    context['countries'] = countries
    return render(request, 'backend/country/country.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def createCountry(request):
    context = {}
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get-country')
    context['form'] = form
    return render(request, 'backend/country/createCountry.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def updateCountry(request, pk):
    context = {}
    country = Country.objects.get(id=pk)
    image_path = country.image.path
    form = CountryForm(instance=country)
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            if len(request.FILES) > 0:
                if len(country.image) > 0:
                    os.remove(image_path)
            form.save()
            return redirect('get-country')
    context['form'] = form
    return render(request, 'backend/country/createCountry.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def deleteCountry(request, pk):
    country = Country.objects.get(id=pk)
    image_path = country.image.path
    if len(country.image) > 0:
        os.remove(image_path)
    country.delete()
    return redirect('get-country')



########## category ######################

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def getCategory(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'backend/category/category.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def createCategory(request):
    context = {}
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get-category')
    context['form'] = form
    return render(request, 'backend/category/createCategory.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def updateCategory(request, pk):
    context = {}
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('get-category')
    context['form'] = form
    return render(request, 'backend/category/createCategory.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('get-category')


########## games ######################

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def getGamesList(request):
    context = {}
    games = Game.objects.all()
    context['games'] = games
    return render(request, 'backend/game/game.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def createGame(request):
    context = {}
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get-game')
    context['form'] = form
    return render(request, 'backend/game/createGame.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def updateGame(request, pk):
    context = {}
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('get-game')
    context['form'] = form
    return render(request, 'backend/game/createGame.html', context)

@login_required(login_url='login-view')
@allowed_users(allowed_roles=['Admin'])
def deleteGame(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('get-game')

