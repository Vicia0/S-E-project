from django.urls import path
from webapp.views import *
from templates import snippets
urlpatterns = [
    #path('', views.index, name = 'index'),
    path('', home, name = 'home'),
    path('check', check, name = 'check'),
    path('passenger-login/', passenger_login, name = 'passenger_login'),
    path('driver-login/', driver_login, name = 'driver_login'),
    path('driver-homepage/', driver_homepage, name='driver_homepage')
    #path('passenger-login/', passenger_login, name = 'passenger-login'),
    #path('home', views.home, name='home')
]