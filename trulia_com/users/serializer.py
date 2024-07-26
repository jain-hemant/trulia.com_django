from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__' #['email','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
