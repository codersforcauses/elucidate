from rest_framework import serializers
from api.apps.users.models import User

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email")
