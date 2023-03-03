from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions

from users.serializers import UserRegistrationSerializer
from users.viewsets import CreateViewSet

User = get_user_model()


class UserRegistrationViewSet(CreateViewSet):
    """
    A viewset that registers a new user.
    """
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
