from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import UserModel


class UserResgitrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(max_length=128, required=True)
    password_confirmation = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = UserModel
        fields = ("username", "email", "password")

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, value):
        del value["password_confirmation"]
        return UserModel.objects.create(**value)
