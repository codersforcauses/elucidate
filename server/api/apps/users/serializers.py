from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password"]

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs["username"]
        ).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Username already exists")

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise serializers.ValidationError(detail="Email already exists")

        phone_number_exists = User.objects.filter(
            phone_number=attrs["phone_number"]
        ).exists()
        if phone_number_exists:
            raise serializers.ValidationError(
                detail="Phone number already exists"
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
