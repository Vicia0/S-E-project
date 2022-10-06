from django.urls import path
from webapp.views import *

urlpatterns = [
    #path('', views.index, name = 'index'),
    path('', home, name = 'home'),
    path('check', check, name = 'check'),
    #path('home', views.home, name='home')
]