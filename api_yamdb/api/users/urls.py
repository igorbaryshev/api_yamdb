from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import (UserRegistrationAPIView,
                         UserViewSet, UserProfileViewSet)

users_view = UserViewSet.as_view({'get': 'list', 'post': 'create'})
user_view = UserViewSet.as_view(
    {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
)
user_profile_view = UserProfileViewSet.as_view(
    {'get': 'retrieve', 'patch': 'partial_update'}
)

urlpatterns = [
    path('v1/users/', users_view, name='users_api'),
    path('v1/users/me/', user_profile_view, name='user_profile_api'),
    re_path(
        r'^v1/users/(?P<username>[\w.@+-]{1,150})/$',
        user_view,
        name='user_api'
    ),
    path('v1/auth/signup/',
         UserRegistrationAPIView.as_view(),
         name='signup_api'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain'),
]
