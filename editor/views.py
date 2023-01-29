from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("Homepage")
    return response

def create(request):
    response = HttpResponse("Create new pages here")
    return response

def browse(request):
    response = HttpResponse("Browse created pages here")
    return response