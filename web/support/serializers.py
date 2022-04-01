from rest_framework import serializers, validators
from .models import Support

# @/get | @/post | @/put | @/delete


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"
