from rest_framework import serializers, validators
from .models import Event

# @/get | @/post | @/put | @/delete


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        extra_kwargs = {
            "date_created": {"read_only": True},
            "date_modified": {"read_only": True},
        }
