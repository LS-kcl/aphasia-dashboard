# Generated by Django 4.1.5 on 2023-03-07 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_alter_sentence_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optional_description', models.CharField(blank=True, max_length=520)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=520)),
                ('parent_selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.imageselection')),
            ],
        ),
    ]