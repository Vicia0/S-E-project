from django import forms
from .models import the_rideForm
from django.forms import ModelForm


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
