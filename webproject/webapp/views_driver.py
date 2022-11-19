from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #csrf errors

#DRIVER PAGES
#Home
def driver_homepage(request):
    context = {}
    return render(request, "driver-homepage.html",{'name':'Martin'} #context)
    )

