from rest_framework import serializers
from users.models import *
from django.contrib.auth import get_user_model

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'author', 'category', 'image', 'date_created', 'text')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', )

# class PropertySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyModel
#         fields = ('id', 'name', 'description', 'price', 'address', 'property_type', 'status', 'area', 'beds', 'baths',
#                   'garage', 'video', 'floor_plans', 'image', 'locationmaps', 'user', 'create_time')
#
#
#
# class AgentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Agent
#         fields = ('id', 'user', 'name', 'profession', 'image', 'bio', 'phone', 'mobile', 'email', 'skype',
#                   'facebook', 'twitter', 'instagram', 'linkedin')
#
#
#
#
# class CommentssSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Comments
#         fields = ('id', 'news', 'user', 'created', 'name', 'email', 'website', 'comment', 'approved', 'best')
#
# class propertySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyCategory
#         fields = ('id', 'name', 'slug')
