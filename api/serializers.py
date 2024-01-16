# usermanagement/serializers.py

from rest_framework import serializers
from .models import UserProfile, MiniTest

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'name']

class MiniTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniTest
        fields = '__all__'