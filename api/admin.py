# api/admin.py
from django.contrib import admin
from .models import UserProfile, UserData, MiniTest

admin.site.register(UserData)
admin.site.register(MiniTest)
admin.site.register(UserProfile)
