# from dataclasses import fields
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import *

from dataclasses import fields
from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserCountryForm(forms.ModelForm):
    class Meta:
        model = UserCountry
        fields = ['country']

    def __init__(self, *args, **kwargs):
        super(UserCountryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control focus'
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label