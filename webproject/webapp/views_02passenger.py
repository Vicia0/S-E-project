from .views_000_req import *
#forms
from .forms_01driver import online_Passengers#, online_Passengers
#models
from .models_00User import User
from .models import the_trip, ride_request,approved_request,denied_request
from .models import the_ride #for pulling available drivers
#views login
from .views_00login import *


# DRIVER PAGES
# Home

#lists
def get_username(request):
    global username_p
    if(len(user_passenger)<=0):
        username_p = ""
        messages.info(request, "Systems timeout, Login again")
        return redirect("passenger_login")  # context)
    else:
        username_p = user_passenger[(len(user_passenger)-1)]

all_passenger_registered_trips = []
passenger_trip = {"trip_id":"","username":"","current_area":"","current_stop":"","destination_area":"", "destination_stop":"","d_date":"","d_time":"","number_of_people":""}
def fn_ps_tripdetails(request):
    all_fields = 'no'
    if request.POST:
        try: username = user_passenger[(len(user_passenger)-1)]
        except:
            messages.info(request, "System timeout, Login again")
            return redirect("passenger_login")
        orig_area =request.POST['area_curr']; orig_stop =request.POST['stop_curr']
        dest_area =request.POST['area_dest']; dest_stop =request.POST['stop_dest']
        n_people = request.POST['number_of_people']
        d_date = request.POST['d_date']; d_time=request.POST['d_time']
        print("username: ", username)
        print("user_passenger: ", user_passenger[(len(user_passenger)-1)])
        get_username(request)
        if username=="":
            get_username(request)
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
    get_username(request)
    return render(request, "02_passenger/00_homepage.html", {'form':online_Passengers, "name":username_p})  # context)

def fn_available_drivers(request): 
    all_rides = the_ride.objects.all().order_by('origin_area','origin_stop','destination_area', 'destination_stop','date','time')

    #context = {"form"}
    get_username(request)
    return render(request, "02_passenger/01_00_AvailableDrivers.html", {"all_rides": all_rides, "name":username_p})  # context)


def fn_showride(request,ride_id): 
    ride = the_ride.objects.get(pk=ride_id)
    if request.POST:
        try: 
            copy_passenger_trips(request) #passenger trips list
            driver = ride
            for count in range(0, len(all_passenger_registered_trips)):
                print("user_passenger: ", user_passenger[(len(user_passenger)-1)])
                print("username : ", all_passenger_registered_trips[count]["username"])
                if(all_passenger_registered_trips[count]["username"])==user_passenger[(len(user_passenger)-1)]:
                    username = user_passenger[(len(user_passenger)-1)]
                    orig_area = all_passenger_registered_trips[count]["current_area"]
                    orig_stop = all_passenger_registered_trips[count]["current_stop"]
                    dest_area = all_passenger_registered_trips[count]["destination_area"]
                    dest_stop = all_passenger_registered_trips[count]["destination_stop"]
                    date = all_passenger_registered_trips[count]["d_date"]
                    time = all_passenger_registered_trips[count]["d_time"]
                    n_people = all_passenger_registered_trips[count]["number_of_people"]
                    new_request= ride_request(driver=driver,ride_id=ride_id,passenger=username,current_area = orig_area,current_stop = orig_stop,
                        destination_area = dest_area,destination_stop = dest_stop,d_date =date,d_time = time,number_of_people =n_people)
                    try:
                        print("done")
                        new_request.save()
                        return redirect("TripComfirmation")
                    except:messages.info(request, "System error, retry or change driver") 
            
        except: messages.info(request, "System error, retry")
    context = {"form"}
    get_username(request)
    return render(request, "02_passenger/01_01_ridedetails.html", {"ride": ride, "name":username_p})  # context)

def copy_passenger_trips(request):
    #Copying all passengers so we call passengers info into a dictionary and push it to the requests
    try:
        all_trips = the_trip.objects.all()
        for ps_request in all_trips:
            print("Copying passenger")
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

passeng =[]
def fn_TripComfirmation(request):
    all_approved = approved_request.objects.all()
    all_denied = denied_request.objects.all()
    all_req = ride_request.objects.all()
    possit = ['nop']
    details = []
    if(len(user_passenger)>0):
        try:

            logged_passenger = user_passenger[(len(user_passenger))-1]
            passeng[0]=logged_passenger
            for x in all_approved:
                if(x.passenger == logged_passenger):
                    details = [x.driver, x.ride_id, x.d_date, x.d_time ]
                    possit[0]=['approved'];break
            for x in all_denied:
                if(x.passenger == logged_passenger):
                    details = [x.driver, x.ride_id, x.d_date, x.d_time ]
                    possit[0]=['denied'];break 
            if(possit[0]!='approved' and possit[0]!='denied'):
                for x in all_req:
                    if(x.passenger == logged_passenger):
                        details = [x.driver, x.ride_id, x.d_date, x.d_time ]
                        possit=['None'];break 
            print('possit:',possit[0])             
            if(request.POST):
                return redirect("passenger_homepage")
        except:
            print("System timeout, login ")
    get_username(request)
    context = {"name":username_p, 'all_approved':all_approved, 'all_denied':all_denied, 'position':possit,'logged_passenger':passeng, 'details':details}
    return render(request, "02_passenger/02_TripComfirmation.html", context)  # context)


def fn_TripDetails(request):
    context = {"form"}
    get_username(request)
    return render(request, "02_passenger/03_TripDetails.html", {"name":username_p})  # context)

 

