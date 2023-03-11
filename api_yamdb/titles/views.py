from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from users.permissions import IsAdminOrReadOnly
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitlesSerializer,
    CreateTitleSerializer
)
from .models import Category, Genre, Title
from .custom_filter import TitleFilter
from .custom_view import CustomSet


class CategoriesViewSet(CustomSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenresViewSet(CustomSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesSerializer
        return CreateTitleSerializer
