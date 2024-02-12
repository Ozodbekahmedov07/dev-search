from django.db import models
import uuid
from users.models import Profile


# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          editable=False, unique=True)
    name = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='project-images/', blank=True, null=True,
                              default='static/images/projects-images/default-image.jpg')
    description = models.TextField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField('Tags', blank=True, null=True)
    source_link = models.TextField(max_length=2000, blank=True, null=True)
    demo_link = models.TextField(max_length=2000, blank=True, null=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    VOTES = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)
    body = models.CharField(max_length=200, choices=VOTES, blank=True, null=True)

    def __str__(self):
        return self.text
