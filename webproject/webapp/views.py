from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def index(request,*args,**kwargs):
def home(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "start-page.html", context )
def passenger_login(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "login-passenger.html", context )
def check(request):
    return HttpResponse("Hello world!")

"""def home(request):
    return render(request, r"home.html", {}) """

