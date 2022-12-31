from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Secteur(models.Model):

    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    is_public = models.BooleanField(_('Public'), default=True)

    class Meta:
        verbose_name = _("Secteur")
        verbose_name_plural = _("Secteurs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Secteur_detail", kwargs={"pk": self.pk})


class Entreprise(models.Model):

    manager = models.ForeignKey(
        User,
        related_name = _('gestionnaire'),
        verbose_name= _('Gestionnaire'),
        on_delete= models.CASCADE
    )

    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    secteur = models.ManyToManyField(
        Secteur,
        verbose_name= _('Secteur'), 
        blank=True
        )
    logo = models.ImageField(_('Logo'), upload_to='entreprise/logo', null = True, blank = True)
    adresse = models.CharField(_('Adresse'), max_length=255, null = True, blank = True)
    phone = PhoneNumberField(unique = True, verbose_name="Téléphone")
    fix = PhoneNumberField(verbose_name=_('Fix'), null = True, blank = True)
    email = models.EmailField(unique=True,verbose_name=_('Email'))
    ifu = models.CharField(_('IFU'), max_length = 255, blank = True, null = True)
    autorised = models.BooleanField(_('Autorisé'), default=False, blank = True)
    is_public = models.BooleanField(_('Visible'), default=False, blank = True)
    date_added = models.DateTimeField(_('Date added'), auto_now_add=True, null=True, blank=True)
    date_last_modified = models.DateTimeField(_('Date modification'), auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Entreprise_detail", kwargs={"pk": self.pk})