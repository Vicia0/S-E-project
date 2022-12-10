from django.contrib.auth.forms import UserCreationForm
from .forms_000_req import *
from .models_00User import User

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_admin', 'is_driver', 'is_passenger')

class Passenger_Register(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'full_name','email', 'phone_number','password1', 'password2', 'is_passenger')

class Driver_Register(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    License_ID = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})) 
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('username','full_name','License_ID', 'email', 'phone_number','password1', 'password2', 'is_driver')

