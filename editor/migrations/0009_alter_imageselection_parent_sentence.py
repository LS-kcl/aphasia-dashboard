# Generated by Django 4.1.5 on 2023-03-09 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0008_imageselection_parent_sentence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageselection',
            name='parent_sentence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='editor.sentence'),
        ),
    ]