from django import forms
from phonenumber_field.formfields import PhoneNumberField
from account.models import *
from service.models import *
class EntrepriseAskingForm(forms.Form):
    
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = PhoneNumberField(region="BJ")
    effectif = forms.ModelChoiceField(
        queryset=EntrepriseEffectif.objects.filter(is_visible = True),
        required=True,
        )
    domain = forms.ModelMultipleChoiceField(
        queryset = DomainActivity.objects.filter(is_visible = True),
        required=True,
    )
    link = forms.URLField()
    text = forms.Textarea()
    contact_method_email = forms.BooleanField()
    contact_method_phone = forms.BooleanField()
    type = forms.ModelChoiceField(queryset=ServiceType.objects.all())


class CustomerAskingForm(forms.Form):
    
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = PhoneNumberField(region="BJ")
    text = forms.Textarea()
    contact_method_email = forms.BooleanField()
    contact_method_phone = forms.BooleanField()
    type = forms.ModelChoiceField(queryset=ServiceType.objects.all())