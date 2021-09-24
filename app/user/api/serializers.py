from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    """Serializers for USERS model"""

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encripted password"""
        """Overriding this method as we need to encript the password before
        saving it to the database and here I am going to use our custom create
        user method that I defined in core app"""

        return get_user_model().objects.create_user(**validated_data)


class AuthTokenUserSerializer(serializers.Serializer):
    """Serialize user authentication object"""

    email = serializers.CharField()
    # by default django-rest trim white space but I don't this to happen
    # to our password
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate user"""
        """Overriding validate function to use email from our custom user model
        insted of email to authenticate user"""

        email = attrs.get("email")
        password = attrs.get("password")

        # by default django viewset passes the context into serializer class
        # when a request is made
        user = authenticate(
            request=self.cotext.get("request"),
            username=email,
            password=password
        )

        # if validating failed
        if not user:
            # response a 400 validation error
            message = _("Invalid credentials, Authentication fieled")
            raise ValidationError(message, code="authentication")

        # wehn authentication success
        attrs["user"] = user
        return attrs
