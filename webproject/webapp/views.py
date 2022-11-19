from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #csrf errors

#HOME
def home(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "start-page.html", context )


#CREATE ACCOUNT PAGES 
def fn_CreateAcc_Passenger(request): #Passenger
    context = {}
    return render(request, "create_account/CreateAccount_Passenger.html", context )
def fn_CreateAcc_Driverpart1(request): #Driver
    context = {}
    return render(request, "create_account/CreateAccou-Driverpart1.html", context )
def fn_CreateAcc_Driverpart2(request): #Driver
    context = {}
    return render(request, "create_account/CreateAccou-Driverpart2.html", context )

#LOGIN PAGES 
def fn_passenger_login(request): #Passenger
    context = {}
    return render(request, "login/login-passenger.html", context )

def fn_driver_login(request):
    context = {}
    return render(request, "login/login-driver.html", context )


#check connection
def check(request):
    return HttpResponse("Server successfully connected!")
"""
def home(request):
    return render(request, r"home.html", {}) 
"""

