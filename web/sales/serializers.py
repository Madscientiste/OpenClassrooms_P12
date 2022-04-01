from rest_framework import serializers, validators
from .models import Salesman

# @/get | @/post | @/put | @/delete


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = "__all__"
