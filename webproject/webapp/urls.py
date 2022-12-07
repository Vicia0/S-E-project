from django.urls import path
from webapp.views import *
from webapp.views_account_creation import *
from webapp.views_login import *
from webapp.views_passenger import *
from webapp.views_driver import *
from templates import snippets


urlpatterns = [
    # path('', views.index, name = 'index'),
    path("", home, name="home"),
    path("check", check, name="check"),
    # create account
    # path('Passenger/Register', fn_CreateAcc_Passenger.as_view(), name = 'CreateAccount_Passenger'),
    # path('Driver/Register/', fn_CreateAcc_Driver.as_view(), name = 'CreateAccount_Driver'),
    path("Passenger/Register/", fn_CreateAcc_Passenger, name="CreateAccount_Passenger"),
    path("Driver/Register/", fn_CreateAcc_Driver, name="CreateAccount_Driver"),
    # LOGIN
    path("Passenger/login/", fn_passenger_login, name="passenger_login"),
    path("Driver/loginpage/", fn_driver_login, name="driver_login"),
    # HOMEPAGES
    path("Driver/homepage/", driver_homepage, name="driver_homepage"),
    path("Passenger/homepage/", passenger_homepage, name="passenger_homepage")
    # path('passenger-login/', passenger_login, name = 'passenger-login'),
    # path('home', views.home, name='home')
    # DRIVER LINKS
    # PASSENGER LINKS
]
