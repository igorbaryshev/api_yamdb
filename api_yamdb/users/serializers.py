from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


class UserSignUpSerializer(serializers.Serializer):
    """
    User registration serializer.
    regex excludes name 'me' from allow names
    """
    email = serializers.EmailField(max_length=254)
    username = serializers.RegexField(regex=r'(?i)\b(?!me\b)^[\w.@+-]+\Z',
                                      max_length=150)


class AccessTokenObtainSerializer(TokenObtainSerializer):
    """
    Single token serializer.
    """
    token_class = AccessToken

    def __init__(self, *args, **kwargs):
        super(TokenObtainSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['confirmation_code'] = serializers.CharField()

    def validate_username(self, username):
        return get_object_or_404(User, username=username).username

    def validate(self, attrs):
        attrs.update({'password': ''})
        data = super().validate(attrs)

        confirmation_code = attrs.get('confirmation_code')
        if not default_token_generator.check_token(self.user,
                                                   confirmation_code):
            raise serializers.ValidationError('Wrong confirmation code.')

        token = str(self.get_token(self.user))
        data["token"] = token

        return data


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    User profile serializer.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('role',)
