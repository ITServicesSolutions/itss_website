from django import forms
from service.models import Service 

class ServiceRequestForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    details = forms.CharField(widget=forms.Textarea)
 