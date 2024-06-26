# Generated by Django 4.1.5 on 2023-04-01 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0011_generatedimage_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='set',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
