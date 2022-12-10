from django.contrib import admin
from .models_00User import User
from .models import the_rideForm,the_ride,the_trip, the_tripForm
admin.site.register(User)

admin.site.register(the_rideForm)
admin.site.register(the_ride)
admin.site.register(the_tripForm)
admin.site.register(the_trip)
# Register your models here.

