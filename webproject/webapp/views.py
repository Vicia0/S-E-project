from this import d
from django.http import HttpResponse
from django.shortcuts import render


#home
#def index(request,*args,**kwargs):
def home(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "start-page.html", context )

#passenger
def passenger_login(request):
    context = {}
    return render(request, "login-passenger.html", context )


#driver
def driver_login(request):
    context = {}
    return render(request, "login-driver.html", context )
def driver_homepage(request):
    context = {}
    return render(request, "driver-homepage.html", context)

#check
def check(request):
    return HttpResponse("Hello world!")

"""def home(request):
    return render(request, r"home.html", {}) """

