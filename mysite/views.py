from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.conf import settings
#from .models import Slider_image

def index(request):
    return render(request, 'mysite/index.html')

def about(request):
    return render(request, 'mysite/about.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def services(request):
    return render(request, 'mysite/services.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def project_detail(request):
    return render(request, 'mysite/project_detail.html')