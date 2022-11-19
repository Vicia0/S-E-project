from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #csrf errors


#LOGIN PAGES 
def fn_passenger_login(request): #Passenger
    context = {}
    return render(request, "login/login-passenger.html", context )

def fn_driver_login(request):
    context = {}
    return render(request, "login/login-driver.html", context )

