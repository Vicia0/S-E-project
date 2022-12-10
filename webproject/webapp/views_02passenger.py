from .views_000_req import *
#forms
from .forms_01driver import online_Passengers#, online_Passengers
#models
from .models_00User import User
from .models import the_trip, ride_requests
from .models import the_ride #for pulling available drivers
#views login
from .views_00login import *


# DRIVER PAGES
# Home
global ps_username
ps_username = "user_passenger"
#lists
all_passenger_registered_trips = []
passenger_trip = {"trip_id":"","username":"","current_area":"","current_stop":"","destination_area":"", "destination_stop":"","d_date":"","d_time":"","number_of_people":""}
all_passenger_requests = []
passenger_details = {"trip_id":"","driver":"","username":"","current_area":"","current_stop":"","destination_area":"", "destination_stop":"","d_date":"","d_time":"","number_of_people":""}
def fn_ps_tripdetails(request):
    all_fields = 'no'
    if request.POST:
        username = "user_passenger"
        orig_area ="request.POST['area_curr']"; orig_stop ="request.POST['stop_curr']"
        dest_area ="request.POST['area_dest']"; dest_stop ="request.POST['stop_dest']"
        n_people = "request.POST['number_of_people']"
        d_date = "request.POST['d_date']"; d_time=" request.POST['d_time']"
        if username=="":
            messages.info(request, "Invalid username")
        else:
            if orig_area == "" or orig_stop=="":
                messages.info(request, "Choose your current location")
            else:
                if dest_area == "" or dest_stop=="":
                    messages.info(request, "Choose your destination")
                else:
                    if n_people=="" or n_people=="Select people":
                        messages.info(request, "Choose number of people")
                    else:
                        if d_date == "":
                            messages.info(request, "Incorrect date")
                        else:
                            if d_time =="":
                                messages.info(request, "Incorrect time")
                            else:
                                all_fields='yes'
        if all_fields == 'yes':
            new_trip= the_trip(passenger = username,current_area = orig_area,current_stop = orig_stop,destination_area = dest_area,destination_stop = dest_stop,d_date =d_date,d_time = d_time,number_of_people =n_people )
            try:
                new_trip.save()
                return redirect("available_drivers")
            except:messages.info(request, "Error submitting the form")            
    return render(request, "02_passenger/00_homepage.html", {'form':online_Passengers})  # context)

def fn_available_drivers(request): 
    all_rides = the_ride.objects.all().order_by('origin_area','origin_stop','destination_area', 'destination_stop','date','time')

    #context = {"form"}
    return render(request, "02_passenger/01_00_AvailableDrivers.html", {"all_rides": all_rides})  # context)


def fn_showride(request,ride_id): 
    ride = the_ride.objects.get(pk=ride_id)
    if request.POST:
        try: 
            copy_passenger_trips(request) #passenger trips list
            driver = ride
            for count in range(0, len(all_passenger_registered_trips)):
                print("ps_username: ", ps_username)
                print("username : ", all_passenger_registered_trips[count]["username"])
                if(all_passenger_registered_trips[count]["username"])==ps_username:
                    username = ps_username
                    orig_area = all_passenger_registered_trips[count]["current_area"]
                    orig_stop = all_passenger_registered_trips[count]["current_stop"]
                    dest_area = all_passenger_registered_trips[count]["destination_area"]
                    dest_stop = all_passenger_registered_trips[count]["destination_stop"]
                    date = all_passenger_registered_trips[count]["d_date"]
                    time = all_passenger_registered_trips[count]["d_time"]
                    n_people = all_passenger_registered_trips[count]["number_of_people"]
            new_request= ride_requests(driver=driver,passenger=username,current_area = orig_area,current_stop = orig_stop,
                destination_area = dest_area,destination_stop = dest_stop,d_date =date,d_time = time,number_of_people =n_people)
            try:
                return redirect("TripComfirmation")
            except:messages.info(request, "System error, retry or change driver") 
        except: messages.info(request, "System error, retry")
    context = {"form"}
    return render(request, "02_passenger/01_01_ridedetails.html", {"ride": ride})  # context)

def copy_passenger_trips(request):
    try:
        all_trips = the_trip.objects.all()

        for ps_request in all_trips:
            passenger = ps_request.passenger
            or_area=ps_request.current_area;or_stop=ps_request.current_stop
            dest_area = ps_request.destination_area; dest_stop=ps_request.destination_stop
            date = ps_request.d_date; time = ps_request.d_time
            n_people = ps_request.number_of_people
            trip_details = dict(passenger_trip)
            trip_details["username"]=passenger
            trip_details["current_area"]=or_area
            trip_details["current_stop"]=or_stop
            trip_details["destination_area"]=dest_area
            trip_details["destination_stop"]=dest_stop
            trip_details["d_date"]=date; trip_details["d_time"]=time
            trip_details["number_of_people"]=n_people
            all_passenger_registered_trips.append(trip_details)  
    except:
        messages.info(request, "Error, copying passenger trip")


def copy_passenger_requests():
    all_requests = ride_requests.objects.all().order_by('ride_id')
    for request in all_requests:
        id_ride = request.ride_id;passenger = request.passenger; driver = request.driver
        or_area=request.current_area;or_stop=request.current_stop
        dest_area = request.destination_area; dest_stop=request.destination_stop
        date = request.d_date; time = request.d_time
        n_people = request.number_of_people
        pass_details = passenger_details.copy
        pass_details["trip_id"] = id_ride
        pass_details["username"]=passenger
        pass_details["driver"]=driver
        pass_details["current_area"]=or_area
        pass_details["current_stop"]=or_stop
        pass_details["destination_area"]=dest_area
        pass_details["destination_stop"]=dest_stop
        pass_details["d_date"]=date;pass_details["d_time"]=time
        pass_details["number_of_people"]=n_people
        all_passenger_requests.append(pass_details)


def fn_TripComfirmation(request):
    context = {"form"}
    return render(request, "02_passenger/02_TripComfirmation.html", {"name": "username"})  # context)

def fn_TripDetails(request):
    context = {"form"}
    return render(request, "02_passenger/03_TripDetails.html", {"name": "username"})  # context)

 

