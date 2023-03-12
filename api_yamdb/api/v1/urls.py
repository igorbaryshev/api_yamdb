from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
)
from users.views import UserSignUpAPIView, UserViewSet, token_obtain

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('', include(router.urls), name='api-root'),
    path('auth/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('auth/token/', token_obtain, name='token'),
]
