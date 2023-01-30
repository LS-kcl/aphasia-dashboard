from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def browse(request):
    return render(request, 'browse.html')