from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #csrf errors

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
