from django.apps import AppConfig
from .socialaccount_providers import ready


class SocialAuthConfig(AppConfig):
    name = 'social_auth'

    def ready(self):
        ready(self.get_setup())