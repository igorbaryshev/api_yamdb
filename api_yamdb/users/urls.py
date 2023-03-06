from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import (UserRegistrationAPIView,
                         UserViewSet, UserProfileViewSet)

app_name = 'users'

users_view = UserViewSet.as_view({'get': 'list', 'post': 'create'})
user_view = UserViewSet.as_view(
    {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
)
user_profile_view = UserProfileViewSet.as_view(
    {'get': 'retrieve', 'patch': 'partial_update'}
)

urlpatterns = [
    path('users/', users_view, name='users_api'),
    path('users/me/', user_profile_view, name='user_profile_api'),
    re_path(
        r'^users/(?P<username>[\w.@+-]{1,150})/$',
        user_view,
        name='user_api'
    ),
    path('auth/signup/',
         UserRegistrationAPIView.as_view(),
         name='signup_api'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain'),
]
