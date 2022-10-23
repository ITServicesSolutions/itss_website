from django import forms
from phonenumber_field.formfields import PhoneNumberField
from account.models import *
class EntrepriseAskingForm(forms.Form):
    
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = PhoneNumberField(region="BJ")
    effectif = forms.ChoiceField(
        queryset=EntrepriseEffectif.objects.filter(is_visible = True),
        required=True,
        )
    domain = forms.MultipleChoiceField(
        queryset = DomainActivity.objects.filter(is_visible = True),
        required=True,
    )
    link = forms.URLField()
    text = forms.Textarea()
    contact_method_email = forms.BooleanField(default=True)
    contact_method_phone = forms.BooleanField(default=True)


class CustomerAskingForm(forms.Form):
    
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = PhoneNumberField(region="BJ")
    text = forms.Textarea()
    contact_method_email = forms.BooleanField(default=True)
    contact_method_phone = forms.BooleanField(default=True)