# Generated by Django 4.1.5 on 2023-03-07 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_imageselection_generatedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageselection',
            name='optional_description',
        ),
        migrations.AddField(
            model_name='imageselection',
            name='images_requested',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageselection',
            name='prompt',
            field=models.CharField(default='One off prompt', max_length=520),
            preserve_default=False,
        ),
    ]