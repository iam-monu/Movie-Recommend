from django.contrib import admin
from django.urls import path
from recommend import views 


urlpatterns = [
    path("",views.index, name='home'),
    path("thriller/",views.thriller, name='thriller'),
    path("comedy/",views.comedy, name='comedy'),
    path("crime/",views.crime, name='crime'),
    path("sc-fi/",views.scfi, name='sc-fi'),

]