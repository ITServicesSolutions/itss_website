from django.urls import path
from .views import *
urlpatterns = [
    path('asking_entreprise', asking_entreprise, name = 'ask-entreprise'),
    path('asking_personnel', asking_personnel, name = 'ask-personnel'),
    
]