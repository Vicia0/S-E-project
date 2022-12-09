from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt #csrf errors


# PASSENGER PAGES
# Home
def passenger_homepage(request):
    context = {}
    return render(request, "02_passenger/00_homepage.html", context)
