# socialaccount_providers.py
from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.providers.facebook.provider import FacebookProvider
from .model_utils import get_model_string
from django.contrib.auth import get_model as get_auth_model

def ready(setup_data):
    model_string = get_model_string('EmailAddress')
    from allauth.account import models
    EmailAddress = models.get_model(*model_string.split('.', 1))

    AbstractBaseUser = get_auth_model('AbstractBaseUser')

    setup_data.socialaccount_providers = {
        'google': {
            'SCOPE': ['openid', 'email', 'profile'],
            'AUTH_PARAMS': {
                'ACCESS_TYPE': 'online',
            }
        },
        'facebook': {
            'SCOPE': ['email'],
            'AUTH_PARAMS': {
                'auth_type': 'reauthenticate',
            }
        }
    }
