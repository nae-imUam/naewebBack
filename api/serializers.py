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

class MiniTestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniTest
        fields = ['id', 'test_number', 'chapter']


class QuizDataUpdateSerializer(serializers.Serializer):
    minitest_id = serializers.IntegerField()
    attempt = serializers.IntegerField()
    status = serializers.CharField(max_length=10)
    percentage = serializers.IntegerField()



class QuizDataRetrieveSerializer(serializers.Serializer):
    minitest_id = serializers.IntegerField()
    result = serializers.DictField()

class UserDataRetrieveSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    quiz_data = QuizDataRetrieveSerializer(many=True)