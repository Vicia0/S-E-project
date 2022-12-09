from django.contrib import admin
from .models import User, available_ride,the_ride
admin.site.register(User)

admin.site.register(available_ride)
admin.site.register(the_ride)

# Register your models here.

