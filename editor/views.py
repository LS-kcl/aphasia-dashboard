from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ParagraphForm
from .models import Paragraph

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        form = ParagraphForm(request.POST)
        # Check if given text is valid
        if form.is_valid():
            text = form.cleaned_data.get('text')
            paragraph = Paragraph.objects.create(text=text)
            return redirect('browse')
        messages.add_message(request, messages.ERROR, "Please enter a valid paragraph")


    # Otherwise create simple unbound form:
    form = ParagraphForm()
    return render(request, 'create.html', {'form':form})

def browse(request):
    return render(request, 'browse.html')