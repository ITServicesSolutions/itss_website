from django.shortcuts import render
from customer.models import *
from service.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


def index(request):
    return render(request, 'administration/pages/index.html')

def our_site(request):
    logo = Logo.objects.count()
    carousel = Carousel.objects.count()
    comment = Comments.objects.count()
    partner = Partner.objects.count()
    service = Service.objects.count()
    context = {
        'logo': logo,
        'carousel':carousel,
        'comment':comment,
        'partner':partner,
        'service':service,
    }
    return render(request, 'administration/pages/site.html', context)

def logo_list(request):
    logos = Logo.objects.all()
    context = {'logos': logos}
    return render(request, 'administration/pages/site/logo_list.html', context)
 
def logo_form(request):
    form = Logo_Form()
    if request.POST:
        form = Logo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('logo_list')
    context = {}
    return render(request, 'administration/pages/site/logo_form.html', context)

def carousel_list(request):
    carousels = Carousel.objects.all()
    context = {'carousels': carousels}
    return render(request, 'administration/pages/site/carousel_list.html', context)

def carousel_form(request):
    carousels = Carousel.objects.all()

    form = Carousel_Form()
    if request.POST:
        form = Carousel_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('carousel_list')
    context = {
        'carousels':carousels,
    }
    return render(request, 'administration/pages/site/carousel_form.html', context)

def partner_list(request):
    partners = Partner.objects.all()
    context = {'partners': partners}
    return render(request, 'administration/pages/site/partner_list.html', context)

def partner_form(request):
    context = {}
    return render(request, 'administration/pages/site/partner_form.html', context)

def formation(request):
    formations = Formation.objects.all()
    context = {
        'formations':formations,
    }
    return render(request, 'administration/pages/formations/formation.html', context)

def add_formation(request):
    categories = CategoryFormation.objects.all()

    form = Formation_Form()
    if request.POST:
        form = Formation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('formations')


    context = {
        'categories':categories,
    }
    return render(request, 'administration/pages/formations/add.html', context)

def comments_list(request):
    comments = Comments.objects.filter(is_public=True)
    context = {'comments': comments}
    return render(request, 'administration/pages/site/comments_list.html', context)


def comment_add(request):

    form = Comment_Form()
    if request.POST:
        form = Comment_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('comments_list')


    context = {
    }
    return render(request, 'administration/pages/site/comments_add.html', context)


def partners_list(request):
    partners = Partner.objects.filter(is_public=True)
    context = {'partners': partners}
    return render(request, 'administration/pages/site/partner_list.html', context)


def partner_add(request):

    form = Partners_Form()
    if request.POST:
        form = Partners_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('partners_list')


    context = {
    }
    return render(request, 'administration/pages/site/partner_form.html', context)


def ListeService(request):
    services = Service.objects.filter()
    context = {'services': services}
    return render(request, 'administration/pages/site/service_list.html', context)


def AjoutService(request):
    types = TypeService.objects.all()

    form = Service_Form()
    if request.POST:
        form = Service_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('service_liste')


    context = {
        'types':types
    }
    return render(request, 'administration/pages/site/service_add.html', context)

def ModifierService(request,id):
    types = TypeService.objects.all()
    service = Service.objects.get(id=id)

    form = ModifierService_Form(
        instance=service,
        initial={
            'type':service.type,
            'name':service.name,
            'description':service.description,
            'icone':service.icone,
            'is_public':service.is_public,
            'is_principal':service.is_principal
        }
        
    )
    if request.POST:
        form = ModifierService_Form(request.POST, 
                instance=service,
                initial={
                    'type':service.type,
                    'name':service.name,
                    'description':service.description,
                    'icone':service.icone,
                    'is_public':service.is_public,
                    'is_principal':service.is_principal
                })
        if form.is_valid():
            form.save() 
            return redirect('service_liste')


    context = {
        'form':form,
        'types':types
    }
    return render(request, 'administration/pages/site/service_edit.html', context)