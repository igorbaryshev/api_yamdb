from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken

from users.tokens import confirmation_code

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)
    username = serializers.RegexField(regex=r'^[\w.@+-]+\Z', max_length=150)
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


class AccessTokenObtainSerializer(TokenObtainSerializer):
    token_class = AccessToken

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['confirmation_code'] = serializers.CharField()
        del self.fields['password']

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise exceptions.NotFound

        return username

    def validate(self, attrs):
        attrs.update({'password': ''})
        data = super().validate(attrs)

        code = attrs.get('confirmation_code')
        token = str(self.get_token(self.user))
        data["token"] = token

        if not confirmation_code.check_token(self.user, code):
            raise serializers.ValidationError('wrong confirmation code.')

        return data

class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'bio', 'role']
