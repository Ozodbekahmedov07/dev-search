from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('projects/', projects, name='projects'),
    path('create-project/', createproject, name='create_project'),
    path('single-project/<str:pk>/', singleproject, name='single_project'),
    path('edit-project/<str:pk>/', updateproject, name='edit_project'),
    path('delete-project/<str:pk>/', delete_project, name='delete_project')
]