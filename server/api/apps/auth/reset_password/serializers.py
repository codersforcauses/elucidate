from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

    def validate_password(self, value):
        validate_password(value)
        return value


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = "email"
