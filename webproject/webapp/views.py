from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt #csrf errors

# HOME
def home(request):
    context = {}
    # i.e context['webname'] = "RBIS"
    return render(request, "start-page.html", context)


# check connection
def check(request):
    return HttpResponse("Server successfully connected!")


"""
def home(request):
    return render(request, r"home.html", {}) 
"""
