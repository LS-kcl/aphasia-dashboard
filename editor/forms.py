from django import forms
from .models import Paragraph, Sentence
# For if regular expressions are needed
# from django.core.validators import RegexValidator

class ParagraphForm(forms.ModelForm):
    # Metadata
    class Meta:
        model = Paragraph
        fields = ['text']

        # Show this paragraph as a text area:
        widgets = {'text':forms.Textarea()}

        # Return an empty label, as we do not want to render
        # the text description
        labels = {'text':''}


class SentenceForm(forms.ModelForm):
    # Metadata
    class Meta:
        model = Sentence
        fields = ['text']

        # Return an empty label, as we do not want to render
        # the text description
        labels = {'text':''}