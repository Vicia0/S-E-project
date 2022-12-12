from .views_000_req import *
from .forms_00register_login import LoginForm
# LOGIN PAGES
user_passenger=[]
user_driver = []
def fn_passenger_login(request):  # Passenger
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_passenger:
                global passenger
                passenger = username
                user_passenger.append(passenger)
                login(request, user)
                return redirect('/Passenger/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "01_login_register/login_passenger.html", {'form': form})


def fn_driver_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            global user_driver
            driver = username
            user_driver.append(driver)
            if user is not None and user.is_driver:
                login(request, user)
                return redirect('/Driver/homepage/')
            else:
                messages.info(request,"username or password is wrong")
        else:
            messages.info(request,"Error validating form")
    return render(request, "01_login_register/login_driver.html", {'form': form})
