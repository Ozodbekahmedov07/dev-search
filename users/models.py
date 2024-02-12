from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profiles/', default='profile.png', blank=True, null=True)

    social_github = models.TextField(blank=True, null=True)
    social_linkedin = models.TextField(blank=True, null=True)
    social_stackoverflow = models.TextField(blank=True, null=True)
    social_twitter = models.TextField(blank=True, null=True)
    social_website = models.TextField(blank=True, null=True)
    social_telegram = models.TextField(blank=True, null=True)
    social_instagram = models.TextField(blank=True, null=True)

    # created = models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.username


class Skills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name


class Inbox(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                  related_name='messages', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=200)
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
