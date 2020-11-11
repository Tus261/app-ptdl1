from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('data_analysis', views.dt),
   path('chart',views.chart),
   path('scatter', views.scatter),
   path('line', views.line),
   path('pie', views.pie),
   path('gantt', views.gantt)
]