from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse



def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

def thriller(request):
    return render(request,'thriller.html')

def comedy(request):
    return render(request,'comedy.html')

def crime(request):
    return render(request,'crime.html')

def scfi(request):
    return render(request,'scfi.html')