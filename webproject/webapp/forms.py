from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Passengers


class CreatePassengerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Passengers
        fields = ['username','email', 'age', 'phonenumber', 'password1','password2']

class PassengerChangeForm(UserChangeForm):
    class Meta:
        model = Passengers
        fields = UserChangeForm.Meta.fields

class CreateDriverForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']
"""
class CreateCarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
"""
