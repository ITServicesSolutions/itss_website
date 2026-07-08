from django.urls import path
from .views import *


urlpatterns = [
    path('', login, name = 'login'),
    path('page_register/', page_register, name = 'page_register'),
    path('mon_compte/', profil, name = 'profil'),
    path('logout/', logout, name = 'logout'),
   
    # path('/', include("social_django.urls", namespace = "social")),
  
  
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('afterregister/', afterregister, name='afterregister'),
    path('passwordconfirm/', passwordconfirm, name='passwordconfirm'),
    path('request-password/', RequestPasswordResetEmail.as_view(), name='request_password'),
    path('reset-password/<uidb64>/<token>/', reset_password_confirm, name = 'reset_user_password'),
    
    path('send-notification/', SendNotificationViewSet.as_view({'post': 'create'}), name='send-notification'),
    path('send_email/', send_email, name='send_email'),
  
    path('social/signup/', signup_redirect, name='signup_redirect'),
]
