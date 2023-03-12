from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

NO_ME_USERNAME_REGEX = r'(?i)\b(?!me\b)^[\w.@+-]+\Z'
USERNAME_MAX_LENGTH = User._meta.get_field('username').max_length
EMAIL_MAX_LENGTH = User._meta.get_field('email').max_length


class UserSignUpSerializer(serializers.Serializer):
    """
    User signup serializer.
    Regex excludes name 'me' from allowed names.
    """
    email = serializers.EmailField(max_length=EMAIL_MAX_LENGTH)
    username = serializers.RegexField(regex=NO_ME_USERNAME_REGEX,
                                      max_length=USERNAME_MAX_LENGTH)


class TokenSerializer(serializers.Serializer):
    """
    Single token serializer.
    """
    username = serializers.RegexField(regex=NO_ME_USERNAME_REGEX,
                                      max_length=USERNAME_MAX_LENGTH)
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
