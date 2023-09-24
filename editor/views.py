# RESTFUL API imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

import requests
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist 
from .forms import ParagraphForm, SentenceForm
from .models import Paragraph, Sentence, Set, GeneratedImage, ImageSelection
from .serializers import ParagraphSerializer, SetPlusSentencesSerializer, SetSerializer, ImageSelectionSerializer, SentenceImageURLOnlySerializer, SetAllChildrenSerializer, GenerateImageSerializer, SentenceAndImageSelectionSerializer, ImageSelectionSerializerIDOnly
from gTTS.templatetags.gTTS import say
from backend.settings import UNSPLASH_ACCESS_KEY
import random
import openai


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

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            # Refresh and then blacklist token
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ListSets(generics.ListAPIView):
    """ Endpoint for listing all sets """
    permission_classes = [IsAuthenticated]
    serializer_class = SetPlusSentencesSerializer


    # We override the built in get_queryset method to return the objects we want
    def get_queryset(self):
        return Set.objects.all()

class ViewSet(generics.RetrieveAPIView):
    """ Endpoint for returning data on a set specified by id """
    permission_classes = [IsAuthenticated]
    serializer_class = SetPlusSentencesSerializer

    def get_object(self):
        set_id = self.kwargs.get('set_id')

        # Check if set exists, else return exception
        try:
            set = Set.objects.get(pk=set_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            raise Http404
        
        # Return the set object
        return set

class ViewSentence(generics.RetrieveAPIView):
    """ Endpoint for returning data on a set specified by id """
    permission_classes = [IsAuthenticated]
    serializer_class = SentenceAndImageSelectionSerializer

    def get_object(self):
        sentence_id = self.kwargs.get('sentence_id')

        # Check if set exists, else return exception
        try:
            sentence = Sentence.objects.get(pk=sentence_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            raise Http404
        
        # Return the set object
        return sentence

class ViewSetAndImages(generics.RetrieveAPIView):
    """ Endpoint for returning data on a set along with images specified by id, will generate images if none found """
    # Authentication is instead checked on return
    # permission_classes = [IsAuthenticated]
    serializer_class = SetAllChildrenSerializer

    def get_object(self):
        set_id = self.kwargs.get('set_id')

        # Check if set exists, else return exception
        try:
            set = Set.objects.get(pk=set_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            raise Http404

        # Ensure either set is public, or the requesting user owns the set:
        if not set.public and not (self.request.user == set.created_by):
            return Response(data={'message':'You do not have access to view this page'}, status=status.HTTP_403_FORBIDDEN)

        # Get all child sentences
        sentences = Sentence.objects.filter(parent_set=set) 

        # Generate images for each sentence if not owned
        for sentence in sentences:
            if not ImageSelection.objects.filter(parent_sentence=sentence).exists():
                parent_sentence = sentence
                prompt = sentence.text

                try:
                    with transaction.atomic():
                        # Create a new ImageSelection object 
                        image_selection = create_image_selection(parent_sentence=parent_sentence, prompt=prompt, images_requested=3)
                except IntegrityError:
                    return Response(data="Could not create an ImageSelection", status=status.HTTP_403_FORBIDDEN)
        
        # Return the set object
        return set

class ToggleImageSelected(generics.UpdateAPIView):
    """ Endpoint for setting the image of a Sentence """
    permission_classes = [IsAuthenticated]
    serializer_class = GenerateImageSerializer

    def update(self, request, *args, **kwargs):
        generated_image_id = kwargs.get('generated_image_id')

        # If generated image does not exist, return error 404
        try:
            generated_image = GeneratedImage.objects.get(pk=generated_image_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response(data={'message':'GeneratedImage does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Toggle selected
        generated_image.selected = not generated_image.selected
        generated_image.save()

        # Get parent set:
        # parent_image_selection = ImageSelection.objects.get(pk=)
        # Return the entire set:
        # return_serializer = SetAllChildrenSerializer
        return_serializer = GenerateImageSerializer(generated_image)
        return Response(return_serializer.data, status=status.HTTP_200_OK)

class CreateSet(generics.CreateAPIView):
    """ Endpoint for creating new Sets """
    permission_classes = [IsAuthenticated]
    serializer_class = SetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Replace with kwarg passed in from URL
        # Extract prompt and images requested from page
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')

        # Atomically generate and save objects:
        # Either all sentences are saved and set is created, or none are
        try:
            with transaction.atomic():
                # Create sentences from this text, and add to a set
                ## Delimit text
                sentences = text.split(".")
                ## Strip leading and trailing spaces
                stripped_sentences = [sentence.strip() for sentence in sentences]
                ## Filter empty sentences out
                filtered_sentences = [sentence for sentence in stripped_sentences if sentence]
                ## Create set
                set = Set.objects.create(created_by=request.user, title=title,text=text)
                        
                ## For delimited text:
                for sentence in filtered_sentences:
                    print(sentence)
                    ## Create sentence and add to set
                    Sentence.objects.create(
                        parent_set=set,
                        text=sentence,
                        sound_clip=say(language='en-uk', text=sentence)
                    )

        except IntegrityError:
            return Response(data="Could not create a set", status=status.HTTP_403_FORBIDDEN)

        # Return successful response
        # headers = self.get_success_headers(serializer.validated_data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # Instead of returning the validated response back, serialize and send back the new objects
        return_serializer = SetPlusSentencesSerializer(set)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)

class ToggleSetVisibility(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        set_id = kwargs.get('set_id')

        # If set does not exist, do not update
        try:
            set = Set.objects.get(pk=set_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response(data={'message':'Set does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # If user does not own the set, throw 403_FORBIDDEN
        if request.user != set.created_by:
            return Response(data={'message':'User does not have priviliges to change set visibility'}, status=status.HTTP_403_FORBIDDEN)

        # Else toggle visibility
        set.public = not set.public
        set.save()

        # Return serialised set
        return_serializer = SetPlusSentencesSerializer(set)
        return Response(return_serializer.data, status=status.HTTP_200_OK)

class ToggleImageSelectionType(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        image_selection_id = kwargs.get('image_selection_id')

        # If set does not exist, do not update
        try:
            image_selection = ImageSelection.objects.get(pk=image_selection_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response(data={'message':'ImageSelection does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Else toggle generation type
        print(image_selection.ai_generated)
        image_selection.ai_generated = not image_selection.ai_generated
        image_selection.save()
        print(image_selection.ai_generated)

        # Return serialised set
        return_serializer = ImageSelectionSerializer(image_selection)
        return Response(return_serializer.data, status=status.HTTP_200_OK)

class CreateImageSelection(generics.CreateAPIView):
    """ Endpoint for generating images """  
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSelectionSerializerIDOnly

    # Override create function to generate images
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get image selection and parent sets
        image_selection_id = kwargs.get('image_selection_id')
        old_image_selection = ImageSelection.objects.get(pk=image_selection_id)
        parent_sentence = old_image_selection.parent_sentence
        prompt = old_image_selection.prompt
        ai_generated = old_image_selection.ai_generated

        images_requested = 3

        # We do not acccept calls for more than 3 images
        if images_requested > 3:
            return Response(data="Cannot request more than 3 images", status=status.HTTP_403_FORBIDDEN)

        # We do not acccept calls for less than 1 image
        if images_requested < 1:
            return Response(data="Cannot request less than 1 image", status=status.HTTP_403_FORBIDDEN)

        # We atomically generate and save objects:
        # Either all images are saved and set is created, or none are
        try:
            with transaction.atomic():
                # Delete old image selection
                old_image_selection.delete()
                # Create a new ImageSelection object 
                image_selection = create_image_selection(parent_sentence=parent_sentence, prompt=prompt, images_requested=images_requested, ai_image=ai_generated)
        except IntegrityError:
            return Response(data="Could not create an ImageSelection", status=status.HTTP_403_FORBIDDEN)

        # Return successful response
        # headers = self.get_success_headers(serializer.validated_data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # Instead of returning the validated response back, serialize and send back the new objects
        return_serializer = ImageSelectionSerializer(image_selection)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)



class CreateParagraph(generics.CreateAPIView):
    """ Endpoint for creating new Paragraphs """
    permission_classes = [IsAuthenticated]
    serializer_class = ParagraphSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to save paragraph to db
        try:
            with transaction.atomic():
                serializer.save()
        except IntegrityError:
            return Response(data="Could not save the Paragraph", status=status.HTTP_403_FORBIDDEN)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DeleteSet(generics.DestroyAPIView):
    """ Endpoint for deleting sets """
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'set_id'

    def destroy(self, request, *args, **kwargs):
        set_id = kwargs.get('set_id')

        # Check if set exists, else return exception
        try:
            set = Set.objects.get(pk=set_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response(data={'message':'Set does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete set and return success
        set.delete()
        return Response(data={'message':'Set deleted successfully'}, status=status.HTTP_200_OK)

class DeleteSentence(generics.DestroyAPIView):
    """ Endpoint for deleting sentences """
    # Currently we do not require authentication:
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'sentence_id'

    def destroy(self, request, *args, **kwargs):
        sentence_id = kwargs.get('sentence_id')

        # Check if sentence exists, else return exception
        try:
            sentence = Sentence.objects.get(pk=sentence_id)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response(data={'message':'Sentence does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete sentence and return success
        sentence.delete()
        return Response(data={'message':'Sentence deleted successfully'}, status=status.HTTP_200_OK)

#### Helper functions:
def generate_ai_image(prompt, number_to_generate):
    # Use prompt to query an AI generated image
    # TODO: Add timeout or error handling when method not allowed
    response = openai.Image.create(
        prompt=prompt,
        n=number_to_generate,
        size="512x512"
    )
    return response["data"]

    # Testing line
    # return ["https://picsum.photos/id/%s/300" %str(random.randint(0,300))]

def query_unsplash_image(prompt, number_to_generate):
    # Create query string to append to url
    query_string = "?query=" + prompt.replace(" ", "+") + "&per_page=" + str(number_to_generate)
    url = "https://api.unsplash.com/search/photos" + query_string
    header = {
        "Content-Type":"application/json",
        "Authorization":"Client-ID " + UNSPLASH_ACCESS_KEY,
    }
    
    response = requests.get(url,headers=header)
    response_json = response.json()
    return response_json["results"]

    # Testing line
    # return [
    #     "https://picsum.photos/id/%s/300" %str(random.randint(0,300)),
    #     "https://picsum.photos/id/%s/300" %str(random.randint(0,300)),
    #     "https://picsum.photos/id/%s/300" %str(random.randint(0,300))
    # ]

def create_image_selection(parent_sentence, prompt, images_requested, ai_image=True):
    print("Entered create image selection")
    image_selection = ImageSelection.objects.create(parent_sentence=parent_sentence, prompt=prompt, images_requested=images_requested, ai_generated=ai_image)
    
    if ai_image:
        print("generating ai image")
        # Generate number of images required and add to set
        image_urls = generate_ai_image(prompt, images_requested)
        print(image_urls)

        for url in image_urls:
            generated_image = GeneratedImage.objects.create(parent_selection=image_selection, url=url["url"])
    else:
        image_urls = query_unsplash_image(prompt, images_requested)

        for url in image_urls:
            urls_dictionary = url["urls"]
            generated_image = GeneratedImage.objects.create(parent_selection=image_selection, url=urls_dictionary["raw"])


    return image_selection