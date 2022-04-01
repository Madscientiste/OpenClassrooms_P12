from rest_framework import serializers, validators
from .models import Client

# @/get | @/post | @/put | @/delete


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {
            "phone": {"required": False},
            "date_created": {"read_only": True},
            "date_modified": {"read_only": True},
        }
