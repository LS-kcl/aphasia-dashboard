from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator


# The raw text to be input by the user
class Paragraph(Model):
    # Store text as charfield
    text = models.CharField(
        blank=False,
        max_length=520,
    )

class Set(Model):
    # A set containing all sentences for a page
    title = models.CharField(
        blank=False,
        max_length=255,
    )

class Sentence(Model):
    # A sentence with an accompanying image
    parent_set = models.ForeignKey(Set, on_delete=models.CASCADE)

    text = models.CharField(
        blank=False,
        max_length=520,
    )

    # Accompanying image as a URL 
    # NOTE: This many cause issues with links not starting with http
    image_url = models.URLField(max_length=200, blank=True, default='https://picsum.photos/id/237/200/300')

class ImageSelection(Model):
    # A selection of various generated images
    
    # The prompt we use to generate these images
    prompt = models.CharField(
        blank=False,
        max_length=520,
    )

    # The number of images we want
    images_requested = models.PositiveIntegerField(
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )


class GeneratedImage(Model):
    # A model to store generated images before saving
    url = models.URLField(
        blank=False,
        max_length=520,
    )
    
    parent_selection = models.ForeignKey(ImageSelection, on_delete=models.CASCADE)
