from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jamPandu(request):
    return HttpResponse('Hi How are you')

def hiHello(request):
    return HttpResponse("I am a Response")

