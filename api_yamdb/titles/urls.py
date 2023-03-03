from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet


router = SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')


urlpatterns = [
    #path('', include('djoser.urls')),
    #path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
