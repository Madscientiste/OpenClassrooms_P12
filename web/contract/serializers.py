from rest_framework import serializers, validators
from .models import Contract

from web.event.models import Event

# @/get | @/post | @/put | @/delete


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "date_modified": {"read_only": True},
            "salesmans": {"read_only": True},
        }

    def create(self, validated_data):
        user = self.context["request"].user

        if hasattr(user, "salesman"):
            validated_data["salesmans"] = [user.salesman]

        return super().create(validated_data)
