from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Entreprise)
admin.site.register(DomainActivity)
admin.site.register(EntrepriseEffectif)
