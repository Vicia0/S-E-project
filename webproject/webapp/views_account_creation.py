from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Create_Driver
from django.views.generic import CreateView
from .models import Passengers
from .forms import CreatePassengerForm
#views
#from .models import CreateDriverForm #, CreateCarForm
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class fn_CreateAcc_Passenger(CreateView): #Passenger
    model = Passengers
    form_class = CreatePassengerForm
    #success_url = pass
    template_name = 'create_account/CreateAccount_Passenger.html'
"""    context = {}
    return render(request, "create_account/CreateAccount_Passenger.html", context )
"""

#Driver part 1
def fn_CreateAcc_Driverpart1(request): 
    messages.info(request,None)
    if request.method=="POST":
        all_fields_valid='No'
        dr_username = request.POST.get('dr_username'); dr_firstname = request.POST.get('dr_firstname');dr_lastname = request.POST.get('dr_lastname')
        dr_email = request.POST.get('dr_email');dr_phonenumber = request.POST.get('dr_phonenumber')
        dr_password1= request.POST.get('dr_password1');dr_password2=request.POST.get('dr_password2')
        
        if (dr_username=="" or dr_firstname=="" or dr_lastname=="" or dr_lastname=="" or dr_email=="" or dr_phonenumber=="" or dr_password1==""):
            messages.info(request,"Important fields are missing")
        else:
            if (dr_password1!=dr_password2): messages.info(request,"Passwords must match")#checking password match
            else:
                try:
                    int(dr_phonenumber)
                    if(int(dr_phonenumber)<0 or int(dr_phonenumber)>9999999999):
                        raise Exception
                    else:
                        if(re.fullmatch(regex, dr_email)):#checking email
                            all_fields_valid='Yes'
                        else:messages.info(request,"Invalid email") 
                except:
                    messages.info(request, "Phone number not valid")        
        if(all_fields_valid =='Yes'):
            new_driver = Create_Driver(username=dr_username, firstname=dr_firstname, lastname=dr_lastname,email=dr_email, phonenumber=dr_phonenumber,password=dr_password1)
            messages.info(request,"All fields correct")      
            try:
                new_driver.save()  
            except: messages.info(request,"User account not created")
    context = {}
    return render(request, "create_account/CreateAccou-Driverpart1.html", context)

#Driver part 2
def fn_CreateAcc_Driverpart2(request):
    """
    form = CreateCarForm()   
    if request.method=="POST":
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_login')
    context = {'form':form}
    """
    context = {}
    return render(request, "create_account/CreateAccou-Driverpart2.html", context)


