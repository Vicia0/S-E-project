from django.urls import path
from webapp.views import *
from webapp.views_passenger import *
from webapp.views_driver import *
from templates import snippets
urlpatterns = [
    #path('', views.index, name = 'index'),
    path('', home, name = 'home'),
    path('check', check, name = 'check'),
    #create account
    path('Passenger-Createaccount', fn_CreateAcc_Passenger, name = 'CreateAccount_Passenger'),
    path('Driver-Createaccount1/', fn_CreateAcc_Driverpart1, name = 'CreateAccount_Driverpart1'),
    path('Driver-Createaccount2/', fn_CreateAcc_Driverpart2, name = 'CreateAccount_Driverpart2'),
    #LOGIN
    path('passenger-loginpage', fn_passenger_login, name = 'passenger_login'),
    path('driver-loginpage/', fn_driver_login, name = 'driver_login'),

    #HOMEPAGES
    path('driver-homepage/', driver_homepage, name='driver_homepage'),
    path('passenger-homepage/', passenger_homepage, name='passenger_homepage')
    #path('passenger-login/', passenger_login, name = 'passenger-login'),
    #path('home', views.home, name='home')

    #DRIVER LINKS


    #PASSENGER LINKS
]