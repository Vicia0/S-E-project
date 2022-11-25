from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

#LOGIN PAGES 
def fn_passenger_login(request): #Passenger
    context = {}
    return render(request, "login/login-passenger.html", context )

def fn_driver_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.info(request,"Username: "+username)
            messages.info(request,"Password: "+password)
            login(request, user)
            return redirect('driver_homepage')
        else:
            messages.info(request,"Username or password is incorrect")
    context = {}
    return render(request, "login/login-driver.html", context )

