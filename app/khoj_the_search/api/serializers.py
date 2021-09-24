from rest_framework import serializers

from core.models import UserInputValue


class InputValueSerializer(serializers.ModelSerializer):
    """Serializes Input value model fields"""

    class Meta:
        model = UserInputValue
        fields = ["input_values", "timestamp", ]
