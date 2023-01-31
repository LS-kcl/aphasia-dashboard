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


class SentenceForm(forms.ModelForm):
    # Metadata
    class Meta:
        model = Sentence
        fields = ['text']