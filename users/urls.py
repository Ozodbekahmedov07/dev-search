from django.urls import path
from .views import *

urlpatterns = [
    path('', developers, name='developers'),
    path('profile/<str:pk>/', userprofile, name='profile'),
    path('account/', useraccount, name='account'),


    path('register/', userregister, name='register'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout'),
    path('edit-account/', edit_account, name='edit_account'),
    path('create-skills/', createskills, name='create_skills'),
    path('edit-skill/<str:pk>/', editskills, name='editskill'),
    path('delete-skill/<str:pk>/', delete_skill, name='delete_skill'),
    path('messages/', inbox_message, name='inbox'),
    path('view-message/<str:pk>/', viewmessage, name='veiwmessage'),

    path('send-message/<str:pk>/', sendmessage, name='send_message'),


]
