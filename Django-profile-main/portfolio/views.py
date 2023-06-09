from django.shortcuts import render
from django.http import HttpResponse

from .models import Portfolio

def index(request):
    #  return HttpResponse("Hello World")
    portfolio = Portfolio.objects.all()
    return render(request,'index.html',{'portfolio':portfolio})

# Create your views here.
