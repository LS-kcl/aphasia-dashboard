from django.db import models
from django.db.models import Model

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

    # Accompanying image in some form here
