from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    User registration serializer.
    """
    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError('this username is not allowed.')
        return username

    class Meta:
        model = User
        fields = ['email', 'username']
