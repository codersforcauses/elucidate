from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = "email"
