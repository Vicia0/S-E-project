from .views_000_req import *
from .forms_00register_login import LoginForm

# LOGIN PAGES
global user_passenger
user_passenger = "passenger"

def fn_passenger_login(request):  # Passenger
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_passenger:
                global user_passenger
                user_passenger =""
                user_passenger = username
                login(request, user)
                return redirect('/Passenger/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "01_login_register/login_passenger.html", {'form': form})

global user_driver
user_driver = "driver"
def fn_driver_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            global user_driver
            user_driver =""
            user_driver = username
            if user is not None and user.is_driver:
                login(request, user)
                return redirect('/Driver/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "01_login_register/login_driver.html", {'form': form})
