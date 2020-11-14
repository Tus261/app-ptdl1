from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render(request, 'pages/home.html')

def dt(request):
   return render(request,'pages/data_analysis.html')


def cot(request):
   return render(request,'pages/cot.html')

def line(request):
   return render(request,'pages/line.html')

def pie(request):
   return render(request,'pages/pie.html')

