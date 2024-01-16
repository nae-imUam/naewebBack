# api/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, default="x")
    name = models.CharField(max_length=255, blank=True, default="0")

    def __str__(self):
        return self.user.username


class UserData(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username


class MiniTest(models.Model):
    test_number = models.PositiveIntegerField(unique=True)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    questions = models.JSONField()

    def __str__(self):
        return f"MiniTest {self.test_number} - {self.class_name} - {self.subject}"