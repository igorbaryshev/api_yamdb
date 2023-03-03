from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet


router = SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls)),
]
