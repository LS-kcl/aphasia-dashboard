from django.shortcuts import render
from django.http import HttpResponse
from .forms import ParagraphForm

def home(request):
    return render(request, 'home.html')

def create(request):
    form = ParagraphForm()
    return render(request, 'create.html', {'form':form})

def browse(request):
    return render(request, 'browse.html')