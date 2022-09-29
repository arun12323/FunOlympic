from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="homepage"),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('live/', livePage, name='live'),
    path('news/', news, name='news'),
    path('savecomment/', saveComment, name="saveComment"),
    path('getComment/', getComment, name="getComment"),
    path('video/',video, name='video')

]