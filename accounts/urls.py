from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginView, name='login-view'),
    path('logout/', logoutCms, name="logout-cms"),
    
    path('country/', getCountry, name="get-country"),
    path('create-country', createCountry, name="create-country"),
    path('update-country/<int:pk>', updateCountry, name="update-country"),
    path('delete-country/<int:pk>', deleteCountry, name="delete-country"),


    path('category/', getCategory, name="get-category"),
    path('create-category', createCategory, name="create-category"),
    path('update-category/<int:pk>', updateCategory, name="update-category"),
    path('delete-category/<int:pk>', deleteCategory, name="delete-category"),


    path('game/', getGamesList, name="get-game"),
    path('create-game/', createGame, name="create-game"),
    path('update-game/<int:pk>', updateGame, name="update-game"),
    path('delete-game/<int:pk>', deleteGame, name="delete-game"),

]
