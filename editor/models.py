from django.db import models
from django.db.models import Model

# The raw text to be input by the user
class Paragraph(Model):
    # Store text as charfield
    text = models.CharField(
        blank=False,
        max_length=520,
    )
