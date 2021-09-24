from django.contrib.auth import get_user_model

from rest_framework import serializers


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
