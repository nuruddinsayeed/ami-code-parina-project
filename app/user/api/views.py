from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.api.serializers import UserSerializer, AuthTokenUserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    """Create a new user to our database"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create API Token for user authentication"""

    serializer_class = AuthTokenUserSerializer
    # set rederer class for Django Rest browsable api
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
