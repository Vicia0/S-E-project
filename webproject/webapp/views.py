from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def index(request,*args,**kwargs):
"""def index(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "RBIS/home.html", context )"""
def home(request):
    context = {}
    #i.e context['webname'] = "RBIS"
    return render(request, "RBIS/home.html", context )
def check(request):
    return HttpResponse("Hello world!")

"""def home(request):
    return render(request, r"home.html", {}) """

