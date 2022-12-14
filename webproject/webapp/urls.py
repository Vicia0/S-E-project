from django.urls import path
from webapp.views import *
from webapp.views_00account_creation import *
from webapp.views_00login import *
from webapp.views_02passenger import *
from webapp.views_01driver import *

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
    path("Driver/login/", fn_driver_login, name="driver_login"),
    # HOMEPAGES
    path("Driver/homepage/", fn_dr_tripdetails, name="driver_homepage"),
    path("Passenger/homepage/", fn_ps_tripdetails, name="passenger_homepage"),
    # path('passenger-login/', passenger_login, name = 'passenger-login'),
    # path('home', views.home, name='home')
    # DRIVER LINKS, pages in order
    path("Driver/Requests/", fn_requests, name="passenger_requests"),
    path("Driver/ActiveRequests/", fn_active_requests, name="passenger_active_requests"),
    path("Driver/ApprovedRequests/", fn_approved_requests, name="passenger_approved_requests"),

    
    path("Driver/Stops/", fn_stops, name="passenger_stops"),
    path("Driver/Dropoffs/", fn_dropoff, name="passenger_dropoffs"),
    # PASSENGER LINKS, pages in order
    path("Passenger/AvailableDrivers/", fn_available_drivers, name="available_drivers"),
    path("Passenger/AvailableDrivers/Showride/<ride_id>", fn_showride, name="showride"),
   
   
    path("Passenger/TripComfirmation/", fn_TripComfirmation, name="TripComfirmation"),
    path("Passenger/TripDetails/", fn_TripDetails, name="TripDetails")
]
