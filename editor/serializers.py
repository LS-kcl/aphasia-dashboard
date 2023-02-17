from .models import Paragraph
from rest_framework import serializers

class ParagraphSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Paragraph
        fields=([
            'text'
        ])


