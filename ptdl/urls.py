from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('data_analysis', views.dt),
   path('cot', views.cot),
   path('line', views.line),
   path('pie', views.pie),
   
]