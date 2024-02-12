from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

@admin.register(Tags)
class AdminTags(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Reviews)
class AdminREVIEW(admin.ModelAdmin):
    list_display = ('id', 'text')