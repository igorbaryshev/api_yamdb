from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from reviews.filters import TitleFilter
from reviews.models import Category, Genre, Review, Title
from reviews.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleCreateSerializer,
    TitleSerializer,
)
from reviews.viewsets import GenreCategoryViewSet
from users.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    @property
    def title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.title.reviews.order_by('pub_date')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    @property
    def review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.review.comments.order_by('pub_date')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.review)


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
