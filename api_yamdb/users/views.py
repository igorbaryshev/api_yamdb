from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdminUser
from users.serializers import UserSerializer, UserSignUpSerializer

User = get_user_model()


class UserSignUpAPIView(GenericAPIView):
    """
    API view that signs up a new user, if it doesn't exist,
    and sends confirmation code to their email,
    if correct credentials are provided.
    """
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = (AllowAny,)

    def send_confirmation_code(self):
        subject = 'Confirmation code.'
        message = default_token_generator.make_token(self.user)
        self.user.email_user(subject, message)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')

        try:
            self.user, _ = self.get_queryset().get_or_create(email=email,
                                                             username=username)
        except IntegrityError:
            raise ValidationError('A user with such email '
                                  'or username already exists.')
        self.send_confirmation_code()

        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    """
    A viewset that allows admin to add or modify users.
    Authenticated users can access and modify
    their profile info at 'users/me/'.
    """
    queryset = User.objects.order_by('username')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    http_method_names = ('get', 'post', 'patch', 'delete')
    lookup_field = 'username'
    lookup_value_regex = r'[\w.@+-]{1,150}'

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request):
        self.kwargs['username'] = request.user.username
        if request.method == 'PATCH':
            serializer = self.get_serializer(request.user, data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=request.user.role)
            return Response(serializer.data)

        return self.retrieve(request)
