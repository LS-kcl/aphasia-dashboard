from .models import Paragraph, Set, Sentence, GeneratedImage, ImageSelection
from rest_framework import serializers

class ParagraphSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Paragraph
        fields=([
            'text'
        ])

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Set
        fields='__all__'

class NoIDSetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Set
        fields=(['title'])

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sentence
        fields='__all__'

class SentenceImageURLOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model=Sentence
        fields=(['image_url'])

class SetPlusSentencesSerializer(serializers.ModelSerializer):
    # Add data of child sentences as a field using a method
    # See: https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    child_sentences = serializers.SerializerMethodField()
    
    class Meta:
        model=Set
        fields='__all__'

    def get_child_sentences(self, obj):
        # Get all child sentences as queryset
        queryset = Sentence.objects.filter(parent_set=obj.id) 

        # Serialize this queryset data
        serializer = SentenceSerializer(queryset, many=True)

        # Return the serialized data
        return serializer.data

class ImageSelectionSerializer(serializers.ModelSerializer):
    # Add data of child image as a field using a method
    # See: https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    child_images = serializers.SerializerMethodField()
    
    class Meta:
        model=ImageSelection
        fields='__all__'

    def get_child_images(self, obj):
        # Get all child images as queryset
        queryset = GeneratedImage.objects.filter(parent_selection=obj.id) 

        # Serialize this queryset data
        serializer = GenerateImageSerializer(queryset, many=True)

        # Return the serialized data
        return serializer.data

class GenerateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneratedImage
        fields='__all__'
