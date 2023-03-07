from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet


router = SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')

urlpatterns = [
    #path('', include('djoser.urls')),
    #path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
