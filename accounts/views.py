from django.shortcuts import render
from django.contrib.auth import login as login_auth, logout as logout_auth, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import *
from .forms import *
from customer.models import *
# Create your views here.

def profil(request):
    context = {}
    return render(request,'accounts/profil.html',context)


def login(request):
    logos = Logo.objects.filter(is_active = True)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('profil')
    context={'logos': logos}
    return render(request, 'accounts/login.html', context)

def register(request):
    logos = Logo.objects.filter(is_active = True)
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user.username= email
            user.save()
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login_auth(request, user)
            return redirect('profil')
        
    context = {'form' : form, 'logos': logos}
    return render(request, 'accounts/register.html', context)

def logout(request):
    logout_auth(request)
    return redirect('home')