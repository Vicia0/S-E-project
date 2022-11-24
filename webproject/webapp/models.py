from django.db import models

# Create your models here.

class Create_Driver(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    
    def __str__(self):
        return self.username


class Car(models.Model):
    car_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_description = models.CharField(max_length=255)

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

'''class CreateDriverForm(UserCreationForm):
    class Meta: 
        model = User
        phonenumber = models.IntegerField(max_length=255)
        fields = ['username','first_name','last_name','phonenumber','email','password1','password2']
'''
"""class CreateDriverForm(UserCreationForm):
        model = Drivers
        fields = ['username','firstname','lastname','email','phonenumber','password1','password2']"""
"""
class CreateCarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
"""
