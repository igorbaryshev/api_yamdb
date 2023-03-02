from django.urls import include, path
from rest_framework.routers import SimpleRouter

from reviews.views import CommentViewSet, ReviewViewSet

v1_router = SimpleRouter()
v1_router.register(r'titles/(?P<titles_id>\d+)/reviews', ReviewViewSet)
v1_router.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
