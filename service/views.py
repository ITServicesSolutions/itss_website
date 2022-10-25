from http import server
from django.shortcuts import render, redirect
from .forms import *
from account.models import *
from django.db.models import Q
from .models import *
from django.core.mail import send_mail
from itss.settings import EMAIL_HOST_USER
# Create your views here.

def asking_entreprise(request):
    domains  = DomainActivity.objects.filter(is_visible=True)
    effectifs = EntrepriseEffectif.objects.filter(is_visible=True)
    form = EntrepriseAskingForm()
    if request.method == 'POST':
        form = EntrepriseAskingForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            effectif = form.cleaned_data['effectif']
            domain = form.cleaned_data['domain']
            link = form.cleaned_data['link']
            text = form.cleaned_data['text']
            contact_method_email = form.cleaned_data['contact_method_email']
            contact_method_phone = form.cleaned_data['contact_method_phone']

            try:
                entreprise = Entreprise.models.filter(Q(email = email) | Q(phone = phone)).exists()
                try:
                    entreprise = Entreprise.objects.get(email=email)
                except Entreprise.DoesNotExist:
                    entreprise = Entreprise.objects.get(phone=phone)
                service = Service.objects.create(
                    entreprise=entreprise,
                    text = text,
                    type = type,
                )
            except Entreprise.DoesNotExist:
                entreprise = Entreprise.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    effectif = effectif,
                    domain = domain,
                    link = link,
                    contact_method_email = contact_method_email,
                    contact_method_phone = contact_method_phone
                )
                service = Service.objects.create(
                    entreprise=entreprise,
                    text = text,
                    type = type,
                )
                subject = "ITSS - Demande de service"
                message = ""
                send_mail(subject, 
                message, EMAIL_HOST_USER, [entreprise.email], fail_silently = False)
            return redirect('home')
    context = {'form':form, 'effectifs': effectifs, 'domains':domains}
    return render(request, 'service/asking_entreprise.html', context)

def asking_personnel(request):
    form = CustomerAskingForm()
    if request.method == 'POST':
        form = CustomerAskingForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            contact_method_email = form.cleaned_data['contact_method_email']
            contact_method_phone = form.cleaned_data['contact_method_phone']

            try:
                customer = Customer.models.filter(Q(email = email) | Q(phone = phone)).exists()
                try:
                    customer = Customer.objects.get(email=email)
                except Entreprise.DoesNotExist:
                    customer = Customer.objects.get(phone=phone)
                service = Service.objects.create(
                    customer=customer,
                    text = text,
                    type = type,
                )
            except Customer.DoesNotExist:
                entreprise = Customer.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email=email,
                    phone=phone,
                    contact_method_email = contact_method_email,
                    contact_method_phone = contact_method_phone
                )
                service = Service.objects.create(
                    customer=customer,
                    text = text,
                    type = type,
                )
            return redirect('home')
    context = {'form':form}
    return render(request, 'service/asking_personnel.html', context)