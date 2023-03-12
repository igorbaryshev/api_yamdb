from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from titles.filters import TitleFilter
from titles.models import Category, Genre, Title
from titles.serializers import (CategorySerializer, GenreSerializer,
                                TitleCreateSerializer, TitleSerializer)
from titles.viewsets import GenreCategoryViewSet
from users.permissions import IsAdminOrReadOnly


class CategoryViewSet(GenreCategoryViewSet):
    queryset = Category.objects.order_by('slug')
    serializer_class = CategorySerializer


class GenreViewSet(GenreCategoryViewSet):
    queryset = Genre.objects.order_by('slug')
    serializer_class = GenreSerializer


class TitleViewSet(ModelViewSet):
    queryset = (Title.objects
                .annotate(rating=Avg('reviews__score'))
                .order_by('id'))
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializer
        return TitleCreateSerializer
