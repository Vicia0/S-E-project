from .models_000_req import *
# Create your models here.

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

class the_tripForm(models.Model):
    d_date = models.DateField()
    d_time = models.TimeField()
    number_of_people = models.CharField(max_length=255)

class the_trip(models.Model):
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger


class ride_request(models.Model):
    ride_id = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['ride_id','driver','passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger

class approved_request(models.Model):
    ride_id = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['ride_id','driver','request_id','passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger


class denied_request(models.Model):
    ride_id = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['ride_id','driver','request_id','passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger

class pickups_table(models.Model):
    ride_id = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['ride_id','driver','request_id','passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger

class dropoff_table(models.Model):
    ride_id = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    passenger = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)
    current_stop = models.CharField(max_length=255)
    destination_area = models.CharField(max_length=255)
    destination_stop = models.CharField(max_length=255)
    d_date = models.CharField(max_length=255)
    d_time = models.CharField(max_length=255)
    number_of_people = models.CharField(max_length=255)
    fields = ['ride_id','driver','request_id','passenger','current_area','current_stop','destination_area', 'destination_stop','d_date','d_time','number_of_people']
    def __str__(self):
        return self.passenger

