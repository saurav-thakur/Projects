from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import fields, widgets

from .models import *


class UserRegisterForm(ModelForm):

    class Meta:
        model = UserModel
        fields = '__all__'
        # widgets = {

        # }


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2']
