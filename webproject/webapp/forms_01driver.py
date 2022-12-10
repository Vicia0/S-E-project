from .forms_000_req import *
from .models import the_rideForm,the_tripForm

#driver
class online_Drivers(ModelForm):
    color =((1,"White"),(2, "Grey"),(3, "Red"),(4, "Brown"),(5, "Yellow"),(6,"Green"), (7,"Blue/Navy Blue"))
    car_color = forms.TypedChoiceField(choices=color, coerce=str)
    date = forms.DateField()#done
    time = forms.TextInput()#done
    seats =((1,"1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),)
    available_seats = forms.TypedChoiceField(choices=seats, coerce=int)#done
    class Meta:
        model = the_rideForm
        """fields = ['driver','car_color','car_plate','origin_area','origin_stop','destination_area',
                 'destination_stop','date','time','available_seats']"""
        fields = ['car_plate','car_color', 'available_seats','date','time']
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

#passenger
class online_Passengers(ModelForm):
    d_date = forms.DateField()#done
    d_time = forms.TextInput()#done
    people =((1,"1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),)
    number_of_people = forms.TypedChoiceField(choices=people, coerce=int)#done
    class Meta:
        model = the_tripForm
        fields = ['number_of_people','d_date','d_time']
        widgets = {
        'd_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

