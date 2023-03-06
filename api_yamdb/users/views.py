from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdminUser, IsUserAccountOwner
from users.serializers import (UserSignUpSerializer,
                               UserSerializer, UserProfileSerializer)
from users.viewsets import RetrieveUpdateViewSet

User = get_user_model()


class UserSignUpAPIView(CreateAPIView):
    """
    API view that signs up a new user, if it doesn't exist,
    and sends confirmation code to their email,
    if correct credentials are provided.
    """
    serializer_class = UserSignUpSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.send_confirmation_code()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_200_OK,
                        headers=headers)

    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')

        user = User.objects.filter(email=email, username=username)

        if not user.exists():
            if User.objects.filter(email=email).exists():
                raise ValidationError(
                    {'email': 'User account with this email already exists.'}
                )
            if User.objects.filter(username=username).exists():
                raise ValidationError(
                    {'username': 'This username is already taken.'}
                )
            self.user = serializer.save()
        else:
            self.user = user[0]

    def send_confirmation_code(self):
        subject = 'Confirmation code.'
        message = default_token_generator.make_token(self.user)
        self.user.email_user(subject, message)


class UserViewSet(ModelViewSet):
    """
    A viewset that allows admin to add or modify users.
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class UserProfileViewSet(RetrieveUpdateViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = (IsUserAccountOwner,)

    def get_object(self):
        obj = self.request.user

        self.check_object_permissions(self.request, obj)

        return obj
