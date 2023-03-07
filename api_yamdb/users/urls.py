from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserSignUpAPIView,UserViewSet

app_name = 'users'

v1_router = SimpleRouter()
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(v1_router.urls), name='users_api'),
    path('auth/signup/', UserSignUpAPIView.as_view(), name='signup_api'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain'),
]
