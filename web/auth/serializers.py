from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=UserModel.objects.all())])
    password = serializers.CharField(write_only=True, max_length=128, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, max_length=128, required=True)

    class Meta:
        model = UserModel
        fields = ("id", "username", "email", "password", "password2")
        extra_kwargs = {"id": {"read_only": True}}

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, value):
        del value["password2"]
        return UserModel.objects.create_user(**value)
