from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ParagraphForm, SentenceForm
from .models import Paragraph, Sentence, Set

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        form = ParagraphForm(request.POST)
        # Check if given text is valid
        if form.is_valid():
            text = form.cleaned_data.get('text')
            paragraph = Paragraph.objects.create(text=text)

            # Create sentences from this text, and add to a set
            ## Delimit text
            sentences = text.split(".")
            ## Create set
            set = Set.objects.create()
            ## For delimited text:
            for sentence in sentences:
                ## Create sentence
                Sentence.objects.create(parent_set=set,text=sentence)
                ## Add to set
            return redirect('pick_images/' + str(set.id))
        messages.add_message(request, messages.ERROR, "Please enter a valid paragraph")


    # Otherwise create simple unbound form:
    form = ParagraphForm()
    return render(request, 'create.html', {'form':form})

def pick_images(request, id):
    set = Set.objects.get(pk=id)
    sentences_queryset = Sentence.objects.filter(parent_set=id).values()
    sentences = [sentence for sentence in sentences_queryset]
    # For each sentence, create a bound form to return:
    sentence_forms = [SentenceForm({'text':sentence['text']}) for sentence in sentences]
    return render(request, 'pick_images.html', {'sentences':sentences, 'sentence_forms':sentence_forms})

def view_page(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'view_page.html')

def browse(request):
    return render(request, 'browse.html')