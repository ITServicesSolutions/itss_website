from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import *
from service.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_admin(user):
    return user.is_superuser


def index(request):
    context = {}
    
    try:
        logos = Logo.objects.filter(is_active=True)
        context['logos'] = logos
    except Exception as e:
        print(f"Error fetching logos: {e}")
        context['logos'] = []
    
    try:
        carousels = Carousel.objects.filter(is_active=True)
        context['carousels'] = carousels
    except Exception as e:
        print(f"Error fetching carousels: {e}")
        context['carousels'] = []
    
    try:
        typeservice = TypeService.objects.filter(is_public=True, name__icontains="service")
        context['typeservice'] = typeservice
        
        principals_services = Service.objects.filter(type__in=typeservice, is_public=True, is_principal=True)
        context['principals_services'] = principals_services
        
        services = Service.objects.filter(type__in=typeservice, is_public=True)
        context['services'] = services
    except Exception as e:
        print(f"Error fetching services: {e}")
        context['principals_services'] = []
        context['services'] = []
    
    try:
        formations = Formation.objects.filter(is_public=True, is_principal=True)
        context['formations'] = formations
    except Exception as e:
        print(f"Error fetching formations: {e}")
        context['formations'] = []
    
    try:
        comments = Comments.objects.filter(is_public=True)
        context['comments'] = comments
    except Exception as e:
        print(f"Error fetching comments: {e}")
        context['comments'] = []
    
    try:
        partners = Partner.objects.filter(is_public=True)
        context['partners'] = partners
    except Exception as e:
        print(f"Error fetching partners: {e}")
        context['partners'] = []
    
    return render(request, 'customer/pages/index.html', context)


"""def index(request):
    logos = Logo.objects.filter(is_active = True)
    carousels = Carousel.objects.filter(is_active = True)
    typeservice = TypeService.objects.filter(is_public = True, name__icontains = "service")
    principals_services = Service.objects.filter(type__in = typeservice, is_public = True, is_principal = True)
    formations = Formation.objects.filter(is_public = True, is_principal = True)
    services = Service.objects.filter(type__in = typeservice, is_public = True)
    comments = Comments.objects.filter(is_public=True)
    partners = Partner.objects.filter(is_public = True)
    context = {
        'carousels': carousels,
        'logos': logos,
        'principals_services': principals_services,
        'formations': formations,
        'services': services,
        'comments': comments,
        'partners': partners,
    }
    return render(request, 'customer/pages/index.html', context)"""

def about(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/about.html', context)

def contact(request):
    logos = Logo.objects.filter(is_active = True)
    submited =False
    if request.method == 'POST':
           
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        
        contact.save()
        return HttpResponseRedirect('?submited=True')
    else:
       
        contact = Contact()
        if 'submited' in request.GET:
            submited = True
   
    context = {'logos': logos, 'submited': submited}
    return render(request, 'customer/pages/contact.html', context)

def teams(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/teams.html', context)

def service(request):
    logos = Logo.objects.filter(is_active = True)
    services = Service.objects.filter(is_public = True)
    context = {
        'logos': logos,
        'services': services,
        }
    return render(request, 'customer/pages/service.html', context)

def formation(request):
    logos = Logo.objects.filter(is_active = True)
    formations = Formation.objects.filter(is_public = True)
    context = {
        'logos': logos,
        'formations': formations
        }
    return render(request, 'customer/pages/formation.html', context)


@login_required(login_url='login')
def request_save(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/request_save.html', context)

@login_required(login_url='login')
def request_service(request):
    logos = Logo.objects.filter(is_active=True)
    context = {'logos': logos}
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # Création d'une nouvelle demande de service
            service_request = ServiceRequest(user=request.user, **form.cleaned_data)
            service_request.save()
            # Vous pouvez rediriger l'utilisateur après la sauvegarde réussie
            return redirect('request_save')
    else:
        form = ServiceRequestForm()
        
    context['form'] = form
    return render(request, 'customer/pages/ask_service.html', context)


@login_required
@user_passes_test(is_admin)    
def demande(request):
    logos = Logo.objects.filter(is_active = True)
    results = Contact.objects.all()
    service_requests = ServiceRequest.objects.all()
    
    context = {'logos': logos, 'data': results, 'service_requests': service_requests}
    return render(request, 'accounts/requests.html', context)

# def affichage(request, contact_id):
#     contact = Contact.objects.get(id=contact_id)
#     contact.affichage()
#     contact.save()
#     return redirect("demande", pk=contact_id)


@login_required(login_url='login')
def consulter(request):
    logos = Logo.objects.filter(is_active = True)
    formations = Formation.objects.filter(is_public = True)
    videos = Video.objects.all()
    context = {
        'logos': logos,
        'formations': formations,
        'videos': videos,
        }
    return render(request, 'customer/pages/consulter.html', context)


def voirplus(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/voirplus.html', context)


