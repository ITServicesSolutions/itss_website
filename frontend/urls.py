from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'home'),
    path('services', services, name = 'services'),
    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact'),
    path('projects', projects, name = 'projects'),
    path('team', team, name = 'team'),
]