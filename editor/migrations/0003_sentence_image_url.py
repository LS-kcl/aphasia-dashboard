# Generated by Django 4.1.5 on 2023-02-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_set_sentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
