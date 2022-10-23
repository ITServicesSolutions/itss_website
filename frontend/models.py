from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from account.models import Customer, User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Comment(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_('Customer'),
        help_text=_('Customer'),
    )
    
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})

class Contact(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_('Customer'),
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    view = models.BooleanField(default=False)
    achive = models.BooleanField(default=False)
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})


class Partner(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ImageField(upload_to='partner')
    description = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Partner_detail", kwargs={"pk": self.pk})
