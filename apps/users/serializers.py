# apps/users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta: fields = ("id","username","email","password"); model = User
    def validate_password(self, value): validate_password(value); return value
    def create(self, data):
        user = User(username=data["username"], email=data["email"])
        user.set_password(data["password"]); user.save(); return user
