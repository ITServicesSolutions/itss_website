from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    phone = PhoneNumberField(unique = True, verbose_name="Téléphone")
    email = models.EmailField(unique = True, null = True, blank = True)

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'

class Customer(models.Model):

    customer_code = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null= True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, verbose_name="Téléphone")
    date_saved = models.DateTimeField(auto_now_add=True, blank=True)
    date_last_activity = models.DateTimeField(auto_now=True)
    contact_method_email = models.BooleanField(default=True, blank=True)
    contact_method_phone = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})

class DomainActivity(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    is_visible=models.BooleanField(default=True)
    class Meta:
        verbose_name = _("DomainActivity")
        verbose_name_plural = _("DomainActivitys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DomainActivity_detail", kwargs={"pk": self.pk})

class EntrepriseEffectif(models.Model):

    interval_range=models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    is_visible=models.BooleanField(default=True)

    class Meta:
        verbose_name = _("EntrepriseEffectif")
        verbose_name_plural = _("EntrepriseEffectifs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EntrepriseEffectif_detail", kwargs={"pk": self.pk})


class Entreprise(models.Model):

    name = models.CharField(max_length=150)
    domain = models.ManyToManyField(
        DomainActivity,
    )
    effectif = models.ForeignKey(
        EntrepriseEffectif,
        on_delete=models.CASCADE,
    )
    link = models.URLField()
    date_saved = models.DateTimeField(auto_now_add=True, blank=True)
    date_last_activity = models.DateTimeField(auto_now=True)
    contact_method_email = models.BooleanField(default=True, blank=True)
    contact_method_phone = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Entreprise_detail", kwargs={"pk": self.pk})
