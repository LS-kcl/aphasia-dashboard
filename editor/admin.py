from django.contrib import admin
from editor.models import Set, Sentence, ImageSelection, GeneratedImage

# Register your models here.
admin.site.register(Set)
admin.site.register(Sentence)
admin.site.register(ImageSelection)
admin.site.register(GeneratedImage)