from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authen.models import User

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        token['is_active'] = user.is_active
        token['username'] = user.username
        token['year'] = user.year
        token['student_code'] = user.student_code
        
        return token


class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, trim_whitespace=False)
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "year",
            "gpa",
            "student_code",
            "program",
            "created_at",
            "is_staff",
            "is_active",
            "last_login"
        ]
        
    @transaction.atomic
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        