from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions

from .models import Category, Genre, Title
from .serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
