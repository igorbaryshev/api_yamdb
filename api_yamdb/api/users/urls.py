from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserRegistrationViewSet, AdminUserViewSet

v1_router = SimpleRouter()
v1_router.register(r'users', AdminUserViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/',
         UserRegistrationViewSet.as_view({'post': 'create'}),
         name='signup'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain'),
]
