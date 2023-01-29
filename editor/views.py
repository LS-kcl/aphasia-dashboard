from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("Homepage")
    return response
