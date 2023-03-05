from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet, GenreViewSet, TitleViewSet


router = SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    #path('', include('djoser.urls')),
    #path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
