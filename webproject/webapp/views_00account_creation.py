from .views_000_req import *
from .forms_00register_login import Driver_Register, Passenger_Register

# views
# from .models import CreateDriverForm #, CreateCarForm
import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def fn_CreateAcc_Driver(request):
    if request.method == 'POST':
        form = Driver_Register(request.POST)
        if form.is_valid():
                user = form.save()
                messages.info(request,"Account successfully created" )
                return redirect('driver_login')
    else:
        form = Driver_Register()
    return render(request,"01_login_register/Register_driver.html", {'form': form})

def accept_terms_privary(request):
    messages.info(request, "Accept Terms and privacy")

def fn_CreateAcc_Passenger(request):
    if request.method == 'POST':
        form = Passenger_Register(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request,"Account successfully created ")
            return redirect('passenger_login')
    else:
        form = Passenger_Register()
    return render(request,"01_login_register/Register_passenger.html", {'form': form})


