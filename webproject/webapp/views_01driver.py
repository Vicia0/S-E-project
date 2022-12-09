from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms_01driver import online_Drivers#, online_Passengers
from .models import *
from .views_00login import *
import datetime
# @csrf_exempt #csrf errors


# DRIVER PAGES
# Home

def fn_trip_details(request):
    #fields = ['username','car','origin_area','origin_stop','destination_area',
    #    'destination_stop','date','time','available_seats']
    all_fields = 'no'
    if request.POST:
        username = user_driver
        orig_area =request.POST['area_curr']; orig_stop =request.POST['stop_curr']
        dest_area =request.POST['area_dest']; dest_stop =request.POST['stop_dest']
        car_plate=request.POST['car_plate']; car_color=request.POST['car_color']
        av_seats = request.POST['available_seats']
        date = request.POST['date']; time= request.POST['time']
        if username=="":
            messages.info(request, "Invalid username")
        else:
            if orig_area == "" or orig_stop=="":
                messages.info(request, "Choose your current location")
            else:
                if dest_area == "" or dest_stop=="":
                    messages.info(request, "Choose your destination")
                else:
                    if car_plate == "" or car_color=="":
                        messages.info(request, "Enter your car details")
                    else:
                        if av_seats=="" or av_seats=="Select seats":
                            messages.info(request, "Choose available seats")
                        else:
                            if date == "":
                                messages.info(request, "Incorrect date")
                            else:
                                if time =="":
                                    messages.info(request, "Incorrect time")
                                else:
                                    all_fields='yes'
        if all_fields == 'yes':
            new_trip= the_ride(driver = username,car_plate = car_plate,car_color = car_color,origin_area = orig_area,origin_stop = orig_stop,destination_area = dest_area,destination_stop = dest_stop,date =date,time = time,available_seats =av_seats )
            try:
                new_trip.save()
                return redirect("passenger_requests")
            except:messages.info(request, "Error submitting the form")            
    return render(request, "02_driver/00_homepage.html", {'form':online_Drivers})  # context)

def fn_requests(request): 
    context = {"form"}
    return render(request, "02_driver/01_requests.html", {"name": "username"})  # context)

def fn_stops(request):
    context = {"form"}
    return render(request, "02_driver/02_stops.html", {"name": "username"})  # context)

 
def fn_dropoff(request):
    context = {"form"}
    return render(request, "02_driver/02_dropoff.html", {"name": "username"})  # context)

 

