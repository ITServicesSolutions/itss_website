from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class TypeService(models.Model):

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null = True, blank = True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("TypeService")
        verbose_name_plural = _("TypeServices")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TypeService_detail", kwargs={"pk": self.pk})

class Service(models.Model):

    type = models.ForeignKey(
        TypeService, 
        verbose_name=_('Type de service'),
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    name = models.CharField(_('Titre'), max_length=255)
    description = models.TextField(_('Description'), null = True, blank = True)
    file = models.FileField(_('File'), null = True, blank = True, upload_to='service/')
    icone = models.CharField(max_length=255, null = True, blank = True, verbose_name=_('Icône'))
    is_public = models.BooleanField(default=True)
    is_principal = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

class CategoryFormation(models.Model):

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null = True, blank = True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("CategoryFormation")
        verbose_name_plural = _("CategoryFormations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CategoryFormation_detail", kwargs={"pk": self.pk})


class Formation(models.Model):

    BANDE = [
    ('recommande', 'Recommandé'),
    ('populaire', 'Populaire'),
    ('nouveau', 'Nouveau'),
]

    category = models.ForeignKey(
        CategoryFormation,
        on_delete=models.CASCADE,
        verbose_name=_('CategoryFormation')
    )
    name = models.CharField(max_length=255, verbose_name=_('Titre'))
    description = models.TextField(_('Description'), null = True, blank=True)
    mode = models.CharField(_('Mode'), null = True, blank=True, max_length= 255)
    duration = models.IntegerField(_('Duration'))
    fichier = models.FileField(_('Fichier'), upload_to="formation", null = True, blank=True)
    certification = models.CharField(_('Certification'), null = True, blank=True, max_length= 255)
    is_public = models.BooleanField(_('IsPublic'), default=True)
    is_principal = models.BooleanField(_('IsPrincipal'), default=False)
    bande = models.CharField(_('Bande'), max_length=50, choices=BANDE, default="nouveau")
    class Meta:
        verbose_name = _("Formation")
        verbose_name_plural = _("Formations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Formation_detail", kwargs={"pk": self.pk})
