from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .models import Category, Genre, Title
from .serializers import CategorySerializer
from users.permissions import IsAdminOrReadOnly
from rest_framework.response import Response


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination 
    lookup_field = 'slug'
