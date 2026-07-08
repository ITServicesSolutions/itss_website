from django.forms import ModelForm, Form
from django import forms
from customer.models import *
from service.models import *
from entreprise.models import *
from accounts.models import *

class Carousel_Form(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ('image','name','description','is_active')

class Logo_Form(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ('image','name','description','is_active','is_black')
 
class Partners_Form(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('name','logo','link','is_public')

class Formation_Form(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ('fichier','name','description','is_public','is_principal','duration','bande','certification','mode')

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('picture','author_full_name','text','is_public','author_role')
        
class Service_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type','name','description','is_public','icone','is_principal')

class ModifierService_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('type','name','description','icone','is_public', 'is_principal')
        