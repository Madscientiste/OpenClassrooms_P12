from rest_framework.permissions import AllowAny
from rest_framework import generics

from .models import UserModel
from .serializers import UserResgitrationSerializer


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserResgitrationSerializer
