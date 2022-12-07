from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_passenger = models.BooleanField('Passenger', default=False)
    is_driver = models.BooleanField('Driver', default=False)
    is_active = models.BooleanField(default=True)