from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import UserModel


class UserResgitrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=UserModel.objects.all())])
    password = serializers.CharField(write_only=True, max_length=128, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, max_length=128, required=True)

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "password_confirmation")

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, value):
        del value["password_confirmation"]
        return UserModel.objects.create_user(**value)
