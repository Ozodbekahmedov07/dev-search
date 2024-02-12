from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from users.models import *
from .serializers import *
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class NewsSetApiView(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Profile.objects.all()
    serializer_class = NewsSerializers

class UserSetApiView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers

#
