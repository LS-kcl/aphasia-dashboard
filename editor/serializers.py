from .models import Paragraph, Set, Sentence
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
        serializer = ParagraphSerializer(queryset, many=True)

        # Return the serialized data
        return serializer.data