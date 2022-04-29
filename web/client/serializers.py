from rest_framework import serializers, validators
from .models import Client

# @/get | @/post | @/put | @/delete


class ClientSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    is_validated = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {
            "phone": {"required": False},
            "date_created": {"read_only": True},
            "date_modified": {"read_only": True},
            "user": {"write_only": True},
            "sales_contact": {"read_only": True},
        }

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_is_validated(self, obj):
        return obj.is_validated

    def create(self, validated_data):
        user = self.context["request"].user

        if user.salesman:
            validated_data["sales_contact"] = user.salesman

        return super().create(validated_data)
