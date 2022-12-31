from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('teams/', teams, name='teams'),
    path('service/', service, name='service'),
    path('formation/', formation, name='formation'),
]
