from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from accounts.models import User
# Create your models here.

class Logo(models.Model):

    image = models.FileField(_('Image'), upload_to="logo/")
    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), null= True, blank=True)
    is_active = models.BooleanField(_('Active'), default=False)
    is_black = models.BooleanField(_('Black'), default=False)

    class Meta:
        verbose_name = _("Logo")
        verbose_name_plural = _("Logos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Logo_detail", kwargs={"pk": self.pk})


class Carousel(models.Model):

    image = models.ImageField(_('Image'), upload_to="Carousel/")
    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), null= True, blank=True)
    is_active = models.BooleanField(_('Active'), default=False)

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Carousel_detail", kwargs={"pk": self.pk})


class Comments(models.Model):
    author_full_name = models.CharField(max_length=50,null = True, blank = True)
    text = models.TextField(null = True, blank = True)
    picture = models.ImageField(upload_to = 'comment/')
    stars = models.IntegerField(null = True, blank = True)
    is_public = models.BooleanField(default=False)
    author_role = models.CharField(max_length=225,null = True, blank = True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.author_full_name)

    def get_absolute_url(self):
        return reverse("Comments_detail", kwargs={"pk": self.pk})

class Partner(models.Model):

    name = models.CharField(max_length=255, verbose_name=_('Nom'))
    logo = models.ImageField(upload_to = 'partner/')
    link = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Partner_detail", kwargs={"pk": self.pk})
