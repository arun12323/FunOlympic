from django.contrib import admin

from home.models import UserCountry
from . import *

admin.site.register(UserCountry)