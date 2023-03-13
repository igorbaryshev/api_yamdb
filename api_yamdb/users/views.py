from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import filters, serializers, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from users.permissions import IsAdminUser
from users.serializers import (
    TokenSerializer,
    UserSerializer,
    UserSignUpSerializer,
)

User = get_user_model()


class UserSignUpAPIView(APIView):
    """
    API view that signs up a new user, if it doesn't exist,
    and sends confirmation code to their email,
    if correct credentials are provided.
    """
    permission_classes = (AllowAny,)

    def send_confirmation_code(self, user):
        subject = 'Confirmation code.'
        message = default_token_generator.make_token(user)
        user.email_user(subject, message)

    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user, _ = User.objects.get_or_create(**serializer.validated_data)
        except IntegrityError:
            raise serializers.ValidationError('A user with such email '
                                              'or username already exists.')
        self.send_confirmation_code(user)

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

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request):
        self.kwargs['username'] = request.user.username

        if request.method == 'PATCH':
            return self.partial_update(request)

        return self.retrieve(request)

    def perform_update(self, serializer):
        if self.action == 'me':
            serializer.save(role=self.request.user.role)
        else:
            serializer.save()


@api_view(['POST'])
@permission_classes([AllowAny])
def token_obtain(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.validated_data['confirmation_code']

    if not default_token_generator.check_token(user, confirmation_code):
        raise serializers.ValidationError('Wrong confirmation code.')

    token = AccessToken.for_user(user)

    return Response(data={'token': str(token)}, status=status.HTTP_200_OK)
