from .views_000_req import *
#forms
from .forms_01driver import online_Drivers#, online_Passengers
#models
from .models_00User import User
from .models import the_ride, ride_request, approved_request, denied_request,pickups_table, dropoff_table
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
                return redirect("passenger_active_requests")
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
        logged_driver = user_driver[(len(user_driver))-1]
        for count in range(0, len(all_passenger_requests)):
            if(all_passenger_requests[count]["driver"])==logged_driver:
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
                except:
                    print("not done")
        try:
            dr_dts_pending_requests = ride_request.objects.all().order_by('ride_id')
            if(request.GET):    
                request_details ='not collected'
                try:
                    p_ride_id = request.GET['id'];logged_driver = logged_driver                    
                    for req_ls in pending_dr_requests:
                        if req_ls['ride_id'] == p_ride_id and req_ls['driver']==logged_driver:
                            for a_request in dr_dts_pending_requests:
                                if a_request.ride_id == p_ride_id:
                                    request_id = a_request.pk; 
                                    try:
                                        database_request = ride_request.objects.get(pk=request_id)
                                        try: 
                                            if(database_request.driver == logged_driver 
                                            and database_request.passenger == req_ls['username']):
                                                request_details='collected'
                                                break
                                        except: print("Stuck here")
                                    except:print("Error gettting infor")
                except:
                    messages.info(request, "System Error, try")
                if(request_details=='collected'):
                    try:
                        the_request = ride_request.objects.get(pk=request_id)
                        x_ride_id = the_request.ride_id
                        x_driver = the_request.driver
                        x_request_id = request_id
                        x_pass = the_request.passenger
                        x_curr_area = the_request.current_area
                        x_curr_stop = the_request.current_stop
                        x_dest_area = the_request.destination_area
                        x_dest_stop = the_request.destination_stop
                        x_date = the_request.d_date
                        x_time = the_request.d_time
                        x_n_people= the_request.number_of_people
                        if(request.GET.get('comfirm')):
                            try:
                                new_approved = approved_request(ride_id = x_ride_id,driver = x_driver,request_id = x_request_id,passenger = x_pass,
                                    current_area = x_curr_area, current_stop = x_curr_stop,destination_area = x_dest_area,
                                    destination_stop = x_dest_stop,d_date = x_date,d_time = x_time,number_of_people = x_n_people)   
                                new_pickup = pickups_table(ride_id = x_ride_id,driver = x_driver,request_id = x_request_id,passenger = x_pass,
                                    current_area = x_curr_area, current_stop = x_curr_stop,destination_area = x_dest_area,
                                    destination_stop = x_dest_stop,d_date = x_date,d_time = x_time,number_of_people = x_n_people)                             
                                try: 
                                    new_approved.save();new_pickup.save()
                                    try: 
                                        the_request.delete()
                                        return redirect("passenger_approved_requests")
                                    except:print("huge error")
                                except:print("not saved")
                            except:
                                print("Error adding the database")
                        if(request.GET.get('decline')):
                            try:
                                new_denied = denied_request(ride_id = x_ride_id,driver = x_driver,request_id = x_request_id,passenger = x_pass,
                                    current_area = x_curr_area, current_stop = x_curr_stop,destination_area = x_dest_area,
                                    destination_stop = x_dest_stop,d_date = x_date,d_time = x_time,number_of_people = x_n_people)
                                try: 
                                    new_denied.save() 
                                    try:
                                        the_request.delete()
                                        return redirect("passenger_approved_requests")
                                    except:
                                        print("huuuge error")
                                except:print("not saved")
                                print("NO\nNO\nNO\nNO")
                            except:
                                print("Error adding the database")
                    except:
                        print("This erros\nThis error\nThis error")
        except:print("convinient error")
    except: messages.info(request, "System error, retry")
    get_username(request)
    n_pending_requests = len(pending_dr_requests)
    d_Driver =""
    context = {"name":username_d, 'n_pending_requests':n_pending_requests, "pending_dr_requests":pending_dr_requests, "d_Driver":d_Driver}
    return render(request, "02_driver/01_01activerequests.html", context, ) 





def copy_passenger_requests(request):
    #Copying all passengers requests so we call passengers requests 
    # and check those that belong to the driver and add them to a dictionary
    try:
        all_requests = ride_request.objects.all().order_by('ride_id')
        all_passenger_requests.clear()
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
    except:
        messages.info(request, "Error, copying passenger trip")


def fn_approved_requests(request):
    #all_approved =  approved_request.objects.all().order_by('current_area','destination_area','current_stop','destination_stop','d_date', 'd_time')
    get_username(request)
    if(len(user_driver)>0):
        try:
            logged_driver = user_driver[(len(user_driver))-1]
            all_approved = pickups_table.objects.filter(driver=logged_driver).values()
            if(request.GET.get('start')):
                return redirect("passenger_stops")
        except:
            messages.info(request, "System timeout, login ")
            return redirect("driver_login") 
    else:
        return redirect("driver_login") 
    context = {"name":username_d, 'all_approved':all_approved}
    return render(request, "02_driver/01_02approvedrequests.html", context)  # context)

def fn_stops(request):
    get_username(request)
    all_approved_requests = pickups_table.objects.all()
    if(len(user_driver)>0):
        logged_driver = user_driver[(len(user_driver))-1]
        all_approved_requests = pickups_table.objects.filter(driver=logged_driver).values()
        if(request.GET):
            this_request_id = int(request.GET['id'])
            this_request = pickups_table.objects.get(pk=this_request_id)
            print("Logged driver:",logged_driver)
            print("this_request.driver",this_request.driver)
            if this_request.driver == logged_driver:
                print("HEYEYEBNJCDJNDH\n NR\nHN\nBHNJ")
                x_ride_id = this_request.ride_id
                x_driver = this_request.driver
                x_request_id = this_request_id
                x_pass = this_request.passenger
                x_curr_area = this_request.current_area
                x_curr_stop = this_request.current_stop
                x_dest_area = this_request.destination_area
                x_dest_stop = this_request.destination_stop
                x_date = this_request.d_date
                x_time = this_request.d_time
                x_n_people= this_request.number_of_people
                new_dropoff = dropoff_table(ride_id = x_ride_id,driver = x_driver,request_id = x_request_id,passenger = x_pass,
                    current_area = x_curr_area, current_stop = x_curr_stop,destination_area = x_dest_area,
                    destination_stop = x_dest_stop,d_date = x_date,d_time = x_time,number_of_people = x_n_people)
                try:
                    new_dropoff.save()
                    this_request.delete()
                    print("droppoff saved")
                except:
                    print("error saving pickup")
                        
    context = {"name":username_d, 'all_approved_requests':all_approved_requests}
    return render(request, "02_driver/02_00stops.html", context)  # context)


def fn_dropoff(request):
    get_username(request)
    all_dropsoff = dropoff_table.objects.all()
    if(len(user_driver)>0):
        logged_driver = user_driver[(len(user_driver))-1]
        all_dropsoff = dropoff_table.objects.all()
        if(request.GET.get('drop')):
            drop_off_id = int(request.GET['id'])
            print("dropp_off id: ", drop_off_id)
            this_request = dropoff_table.objects.get(pk=drop_off_id)
            print("Logged driver:",logged_driver)
            print("this_request.driver",this_request.driver)
            if this_request.driver == logged_driver:
                try:
                    driver_post=the_ride.objects.get(pk=this_request.ride_id)           
                    print("droppoff saved")
                    try:
                        driver_post.delete(); this_request.delete()
                    except:
                        print("error deleting driver post") 
                except:
                    print("error saving pickup")
        elif(request.GET.get('end')):
            return redirect("driver_homepage")

                        
    context = {"name":username_d, 'all_dropsoff':all_dropsoff}
    return render(request, "02_driver/02_01dropoff.html", context)  # context)
 

