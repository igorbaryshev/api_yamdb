from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdminUser
from users.serializers import UserRegistrationSerializer, AdminUserSerializer
from users.tokens import confirmation_code
from users.viewsets import CreateViewSet

User = get_user_model()


class UserRegistrationViewSet(CreateViewSet):
    """
    A viewset that registers a new user.
    """
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
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
            user = serializer.save()
        else:
            user = user[0]

        self.send_confirmation_code(user)

    def send_confirmation_code(self, user):
        subject = 'Confirmation code.'
        message = confirmation_code.make_token(user)
        user.email_user(subject, message)


class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
