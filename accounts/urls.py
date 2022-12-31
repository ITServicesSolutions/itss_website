from django.urls import path
from .views import *
urlpatterns = [
    path('', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('mon_compte/', profil, name = 'profil'),
    path('logout/', logout, name = 'logout'),
]
