from django.urls import include, path

from users.views import UserRegistrationViewSet

urlpatterns = [
    path('v1/auth/signup/',
         UserRegistrationViewSet.as_view({'post': 'create'}),
         name='signup'),
]
