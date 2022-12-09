from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_passenger = models.BooleanField('Passenger', default=False)
    is_driver = models.BooleanField('Driver', default=False)
    is_active = models.BooleanField(default=True)


class the_rideForm(models.Model):
    car_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.CharField(max_length=255)

class the_ride(models.Model):
    driver = models.CharField(max_length=255)
    origin_area = models.CharField(max_length=255)
    origin_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    car_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    available_seats = models.CharField(max_length=255)
    fields = ['driver','car_plate','car_color','origin_area','destination_area', 'destination_stop','date','time','available_seats']
    def __str__(self):
        return self.driver
