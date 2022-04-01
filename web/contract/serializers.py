from rest_framework import serializers, validators
from .models import Contract

# @/get | @/post | @/put | @/delete


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "date_modified": {"read_only": True},
        }