from django.contrib import admin
from .models_00User import User
from .models import the_rideForm,the_ride,the_trip, the_tripForm
from .models import ride_request, approved_request, denied_request, dropoff_table, pickups_table
admin.site.register(User)

admin.site.register(the_rideForm)
admin.site.register(the_ride)
admin.site.register(the_tripForm)
admin.site.register(the_trip)
admin.site.register(ride_request)
admin.site.register(approved_request)
admin.site.register(denied_request)
admin.site.register(dropoff_table)
admin.site.register(pickups_table)

# Register your models here.

