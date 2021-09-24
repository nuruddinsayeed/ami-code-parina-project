from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
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


class UpdateUserAPIView(generics.RetrieveUpdateAPIView):
    """Manage Authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    # here we can define a model as we need to retrieve only the logged in
    # user, So I need to override get object method
    def get_object(self):
        """Return Authenticated user"""

        return self.request.user
