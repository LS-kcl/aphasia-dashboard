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
            # If all forms are valid, create objects, and redirect to new page
            ### Commented out to prevent duplication glitch, look into making this edit the already existing sentences, or clearing first ###
            # for text in forms_submissions:
            #     new_sentence = Sentence(text=text, parent_set=current_set)
            #     new_sentence.save()
                
            return redirect('view_page', id=id)
        
        # If not valid, return error messages
        messages.add_message(request, messages.ERROR, "All sentences must be valid")
        # return redirect('browse')

    set = Set.objects.get(pk=id)
    sentences_queryset = Sentence.objects.filter(parent_set=id).values()
    sentences = [sentence for sentence in sentences_queryset]
    # For each sentence, create a bound form to return:
    sentence_forms = [SentenceForm({'text':sentence['text']}) for sentence in sentences]
    return render(request, 'pick_images.html', {'sentences':sentences, 'sentence_forms':sentence_forms, 'set':set})

def view_page(request, id):
    set = Set.objects.get(pk=id)
    # Get all sentences in the sets:
    sentences = set.sentence_set.all()
    print(sentences)
    return render(request, 'view_page.html', {'sentences':sentences})

def browse(request):
    sets = Set.objects.all()
    return render(request, 'browse.html', {'sets':sets})
