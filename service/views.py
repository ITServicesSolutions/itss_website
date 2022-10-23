from django.shortcuts import render

# Create your views here.

def asking(request):
    context = {}
    return render(request, 'service/asking.html', context)