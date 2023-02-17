from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ParagraphForm, SentenceForm
from .models import Paragraph, Sentence, Set
from gTTS.templatetags.gTTS import say
# import requests
import random


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
            ## Strip leading and trailing spaces
            stripped_sentences = [sentence.strip() for sentence in sentences]
            ## Filter empty sentences out
            filtered_sentences = [sentence for sentence in stripped_sentences if sentence]
            ## Create set
            set = Set.objects.create()
            ## For delimited text:
            for sentence in filtered_sentences:
                ## Create sentence
                Sentence.objects.create(parent_set=set,text=sentence)
                ## Add to set
            return redirect('pick_images', id=set.id)
        messages.add_message(request, messages.ERROR, "Please enter a valid paragraph")


    # Otherwise create simple unbound form:
    form = ParagraphForm()
    return render(request, 'create.html', {'form':form})

def pick_images(request, id):
    if request.method == 'POST':
        print(request.POST)
        # Create a form for each returned value so we can validate them:
        forms_submissions = request.POST.getlist('text')
        print(forms_submissions)
        # Create new forms with the the current set as the parent
        current_set = Set.objects.get(pk=id)
        forms = [SentenceForm({'text':sentence,'parent_set':current_set}) for sentence in forms_submissions]
        print(forms)

        # Check that all forms are valid
        is_valid = [form.is_valid() for form in forms]
        print(is_valid)
        if all(is_valid):
            print("Forms are all valid")

            # If all forms are valid, delete all old objects, create new objects, and redirect to new page
            current_set.sentence_set.all().delete()

            # NOTE: If taking this approach, and simply creating new objects from form input, consider
            #       refactoring from a model form to a regular form
            for text in forms_submissions:
                random_image = "https://picsum.photos/id/%s/300" %str(random.randint(0,300))
                new_sentence = Sentence(text=text, parent_set=current_set, image_url=random_image)
                new_sentence.save()
                
            return redirect('view_page', id=id)
        
        # If not valid, return error messages
        messages.add_message(request, messages.ERROR, "All sentences must be valid")
        # return redirect('browse')

    set = Set.objects.get(pk=id)
    sentences_queryset = Sentence.objects.filter(parent_set=id).values()
    sentences = [sentence for sentence in sentences_queryset]


    # For each sentence, create a bound form to return:
    sentence_forms = [SentenceForm({'text':sentence['text']}) for sentence in sentences]
    # Create list from it
    form_list = list(sentence_forms)

    # For each sentence form, generate three images:
    # API CALLS HERE
    image_array = []
    for form in sentence_forms:
        image1 = "https://picsum.photos/id/%s/300" %str(random.randint(0,300))
        image2 = "https://picsum.photos/id/%s/300" %str(random.randint(0,300))
        image3 = "https://picsum.photos/id/%s/300" %str(random.randint(0,300))
        image_array.append([image1,image2,image3])

    data_zip = zip(form_list, image_array)

    return render(request, 'pick_images.html', {'sentences':sentences, 'sentence_forms':sentence_forms, 'set':set,'data_zip':data_zip})

def view_page(request, id):
    set = Set.objects.get(pk=id)
    # Get all sentences in the sets:
    sentences = set.sentence_set.all()
    print(sentences)

    ### For integration testing ONLY, refactor into the sentence model ASAP ###

    sentence_text = []
    for sentence in sentences:
        sentence_text.append(sentence.text)

    print(sentence_text)
    # For each sentence, create an audio clip
    audio_clips = [say(language='en-uk', text=text) for text in sentence_text]
    ###

    return render(request, 'view_page.html', {'sentences':sentences, 'audio_clips':audio_clips})

def browse(request):
    sets = Set.objects.all()
    return render(request, 'browse.html', {'sets':sets})
