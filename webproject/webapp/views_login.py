from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# LOGIN PAGES
def fn_passenger_login(request):  # Passenger
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_passenger:
                login(request, user)
                return redirect('/Passenger/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "login/login-passenger.html", {'form': form})


def fn_driver_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_driver:
                login(request, user)
                return redirect('/Driver/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "login/login-driver.html", {'form': form})
