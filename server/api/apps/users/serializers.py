from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "grade",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }
