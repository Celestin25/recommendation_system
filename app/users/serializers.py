"""
Serializers for the user API View
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Intake, Course # noqa


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user object
    """
    class Meta:
        model = get_user_model()
        exclude = (
            'groups',
            'is_staff',
            'is_active',
            'last_login',
            'is_superuser',
            'date_modified',
            'user_permissions',
        )
        required_fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
        Create a user with encrypted password and returns the user instance
        """
        return get_user_model().objects.create_user(
            **validated_data, is_active=False
        )

    def update(self, instance, validated_data):
        """
        Update a user, setting the password correctly and return it
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class ActivateAccountSerializer(serializers.Serializer):
    pass
