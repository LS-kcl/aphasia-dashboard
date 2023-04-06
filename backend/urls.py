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
from editor.views import CreateParagraph, CreateSet, ListSets, DeleteSet, DeleteSentence, ViewSet, CreateImageSelection, ToggleImageSelected, ViewSetAndImages, LogoutView, ToggleSetVisibility
from rest_framework import generics
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/pick_images/<int:id>', views.pick_images, name='pick_images'),
    path('create/view_page/<int:id>', views.view_page, name='view_page'),
    path('browse/', views.browse, name='browse'),

    # API URLS
    path('api-auth/', include('rest_framework.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='api_obtain_token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='api_refresh_token'),
    path('api/logout', LogoutView.as_view(), name='api_logout'),
    path('api/create_paragraph', CreateParagraph.as_view(), name='api_create_paragraph'),
    path('api/create_set', CreateSet.as_view(), name='api_create_set'),
    path('api/list_sets', ListSets.as_view(), name='api_list_sets'),
    path('api/view_set/<int:set_id>', ViewSet.as_view(), name='api_view_set'),
    path('api/view_set_and_images/<int:set_id>', ViewSetAndImages.as_view(), name='api_view_set_and_images'),
    path('api/toggle_set_visibility/<int:set_id>', ToggleSetVisibility.as_view(), name='api_toggle_set_visibility'),
    path('api/delete_set/<int:set_id>', DeleteSet.as_view(), name='api_delete_set'),
    path('api/delete_sentence/<int:sentence_id>', DeleteSentence.as_view(), name='api_delete_sentence'),
    path('api/toggle_image_selected/<int:generated_image_id>', ToggleImageSelected.as_view(), name='toggle_image_selected'),
    path('api/generate_prompts/<int:image_selection_id>', CreateImageSelection.as_view(), name='create_image_selection')
]
