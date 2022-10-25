from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from account.models import Customer, Entreprise

# Create your models here.

class ServiceType(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("ServiceType")
        verbose_name_plural = _("ServiceTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ServiceType_detail", kwargs={"pk": self.pk})


class Service(models.Model):

    type = models.ForeignKey(
        ServiceType,
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )

    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    text = models.TextField()
    view = models.BooleanField(default=False)
    achivied = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    date_saved = models.DateTimeField(auto_now_add=True, blank=True)
    date_viewed = models.DateTimeField(blank = True, null=True)
    date_deleted = models.DateTimeField(blank = True, null = True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})
