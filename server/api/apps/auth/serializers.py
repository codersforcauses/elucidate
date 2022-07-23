from api.apps.users.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
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

    def validate_grade(self, value):
        if value < 11 or value > 13:
            raise ValidationError("The grade should be 11, 12 or 13")
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
