from .views_000_req import *
#forms
from .forms_01driver import online_Drivers#, online_Passengers
#models
from .models_00User import User
from .models import the_ride, ride_request
#views login
from .views_00login import user_passenger, user_driver
all_passenger_requests = []
passenger_request = {"ride_id":"","driver":"","username":"","current_area":"","current_stop":"","destination_area":"", "destination_stop":"","d_date":"","d_time":"","number_of_people":""}
pending_dr_requests =[]
pending_request = {"ride_id":"","driver":"","username":"","current_area":"","current_stop":"",
    "destination_area":"", "destination_stop":"","d_date":"","d_time":"","number_of_people":""}
# DRIVER PAGES
# Home
def get_username(request):
    global username_d
    if(len(user_driver)<=0):
        messages.info(request, "Systems timeout, Login again")
        username_d = ""
        return redirect("driver_login")  # context)
        
    else:
        username_d = user_driver[(len(user_driver))-1]

def fn_dr_tripdetails(request):
    #fields = ['username','car','origin_area','origin_stop','destination_area',
    #    'destination_stop','date','time','available_seats']
    all_fields = 'no'
    if request.POST:
        if (len(user_driver)>0):
            try: username = user_driver[(len(user_driver))-1]
            except:
                messages.info(request, "System timeout, Login again")
                return redirect("driver_login")
        orig_area =request.POST['area_curr']; orig_stop =request.POST['stop_curr']
        dest_area =request.POST['area_dest']; dest_stop =request.POST['stop_dest']
        car_plate=request.POST['car_plate']; car_color=request.POST['car_color']
        av_seats = request.POST['available_seats']
        date = request.POST['date']; time= request.POST['time']
        if username=="":
            get_username(request)
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
    get_username(request)
    return render(request, "02_driver/00_homepage.html", {'form':online_Drivers,"name":username_d })  # context)

def fn_requests(request): 
    context = {"form"}
    get_username(request)
    return render(request, "02_driver/01_00requests.html", {"name":username_d })  # context)


def fn_active_requests(request): 
    try: 
        pending_dr_requests.clear()
        copy_passenger_requests(request) #passenger trips list
        logged_driver = user_driver
        for count in range(0, len(all_passenger_requests)):
            print("dr_username: ", logged_driver)
            print("username : ", all_passenger_requests[count]["driver"])
            if(all_passenger_requests[count]["driver"])==logged_driver:
                print("yes")
                driver = logged_driver;ride_id=all_passenger_requests[count]["ride_id"]
                passenger = all_passenger_requests[count]["username"]
                orig_area = all_passenger_requests[count]["current_area"]
                orig_stop = all_passenger_requests[count]["current_stop"]
                dest_area = all_passenger_requests[count]["destination_area"]
                dest_stop = all_passenger_requests[count]["destination_stop"]
                date = all_passenger_requests[count]["d_date"]
                time = all_passenger_requests[count]["d_time"]
                n_people = all_passenger_requests[count]["number_of_people"]
                try:
                    pending_request = {"ride_id":ride_id,"driver":driver,"username":passenger,
                        "current_area":orig_area,"current_stop":orig_stop,"destination_area":dest_area, 
                        "destination_stop":dest_stop,"d_date":date,"d_time":time,"number_of_people":n_people}
                    pending_dr_requests.append(pending_request)
                    n_pending_requests = len(pending_dr_requests)
                    print(pending_dr_requests)
                    print(pending_request)
                    messages.info(request,"done ")
                except:
                    print("not done")
        try:
            all_requests = ride_request.objects.all().order_by('ride_id')
            for x in range(0,len(pending_dr_requests)):
                print(len(pending_dr_requests) , "rounds")
                x =8
                messages.info(request,"rounds")
        except:print("convieniet error")
        """ new_request= ride_request(driver=driver,ride_id=ride_id,passenger=passenger,current_area = orig_area,current_stop = orig_stop,
            destination_area = dest_area,destination_stop = dest_stop,d_date =date,d_time = time,number_of_people =n_people)
        try:
            return redirect("TripComfirmation")
        except:messages.info(request, "System error, retry or change driver")""" 
    
    except: messages.info(request, "System error, retry")
    get_username(request)
    n_pending_requests = len(pending_dr_requests)
    print("n_pending_requests: ",n_pending_requests)
    context = {"name":username_d, 'n_pending_requests':n_pending_requests, "pending_dr_requests":pending_dr_requests}
    return render(request, "02_driver/01_01activerequests.html", context, ) 


def copy_passenger_requests(request):
    #Copying all passengers requests so we call passengers requests 
    # and check those that belong to the driver and add them to a dictionary
    try:
        all_requests = ride_request.objects.all().order_by('ride_id')
        for ps_request in all_requests:
            id_ride = ps_request.ride_id;driver = ps_request.driver
            passenger = ps_request.passenger
            or_area=ps_request.current_area;or_stop=ps_request.current_stop
            dest_area = ps_request.destination_area; dest_stop=ps_request.destination_stop
            date = ps_request.d_date; time = ps_request.d_time
            n_people = ps_request.number_of_people
            request_details = dict(passenger_request)
            request_details["ride_id"] = id_ride
            request_details["driver"]=driver
            request_details["username"]=passenger
            request_details["current_area"]=or_area
            request_details["current_stop"]=or_stop
            request_details["destination_area"]=dest_area
            request_details["destination_stop"]=dest_stop
            request_details["d_date"]=date; request_details["d_time"]=time
            request_details["number_of_people"]=n_people
            all_passenger_requests.append(request_details) 
            print("done copying") 
            messages.info(request,"done copying")
    except:
        messages.info(request, "Error, copying passenger trip")


def fn_approved_requests(request): 
    context = {"form"}
    get_username(request)
    return render(request, "02_driver/01_02approvedrequests.html", {"name":username_d})  # context)


def fn_stops(request):
    context = {"form"}
    return render(request, "02_driver/02_stops.html", {"name":username_d})  # context)

 
def fn_dropoff(request):
    context = {"form"}
    get_username(request)
    return render(request, "02_driver/02_dropoff.html", {"name":username_d})  # context)

 

