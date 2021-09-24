from rest_framework import generics

from user.api.serializers import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    """Create a new user to our database"""

    serializer_class = UserSerializer
