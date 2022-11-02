from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    active = 'home'
    header = 'header-transparent'
    context = {'active': active, 'header': header}
    return render(request, 'customer/home.html', context)

def services(request):
    active = 'services'
    header = ''
    context = {'active': active, 'header': header}
    return render(request, 'customer/services.html', context)

def team(request):
    active = 'team'
    header = ''
    context = {'active': active, 'header': header}
    return render(request, 'customer/team.html', context)

def about(request):
    active = 'about'
    header = ''
    context = {'active': active, 'header': header}
    return render(request, 'customer/about.html', context)

def contact(request):
    active = 'contact'
    header = ''
    context = {'active': active, 'header': header}
    return render(request, 'customer/contact.html', context)

def projects(request):
    active = 'projects'
    header = ''
    context = {'active': active, 'header': header}
    return render(request, 'customer/projects.html', context)

def formation(request):
    context = {}
    return render(request, 'customer/formation.html', context)