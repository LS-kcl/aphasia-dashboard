"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from editor import views
from editor.views import CreateParagraph, CreateSet, ListSets, DeleteSet, DeleteSentence, ViewSet, CreateImageSelection, SetSentenceImage, ViewSetAndImages
from rest_framework import generics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/pick_images/<int:id>', views.pick_images, name='pick_images'),
    path('create/view_page/<int:id>', views.view_page, name='view_page'),
    path('browse/', views.browse, name='browse'),

    # API URLS
    path('api-auth/', include('rest_framework.urls')),
    path('api/create_paragraph', CreateParagraph.as_view(), name='api_create_paragraph'),
    path('api/create_set', CreateSet.as_view(), name='api_create_set'),
    path('api/list_sets', ListSets.as_view(), name='api_list_sets'),
    path('api/view_set/<int:set_id>', ViewSet.as_view(), name='api_view_set'),
    path('api/view_set_and_images/<int:set_id>', ViewSetAndImages.as_view(), name='api_view_set_and_images'),
    path('api/delete_set/<int:set_id>', DeleteSet.as_view(), name='api_delete_set'),
    path('api/delete_sentence/<int:sentence_id>', DeleteSentence.as_view(), name='api_delete_sentence'),
    path('api/set_sentence_image/<int:sentence_id>', SetSentenceImage.as_view(), name='api_set_sentence'),
    path('api/generate_prompts/', CreateImageSelection.as_view(), name='create_image_selection')
]
