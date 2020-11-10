from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render(request, 'pages/home.html')

def dt(request):
   return render(request,'pages/data_analysis.html')
