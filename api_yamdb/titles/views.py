from rest_framework import status, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer, CreateTitleSerializer
from users.permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .custom_filter import GenreFilter


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        slug = request.data.get('slug')
        if slug and Genre.objects.filter(slug=slug).exists():
            return Response({'slug': 'slug already exist'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('id')
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (GenreFilter, DjangoFilterBackend,)
    filterset_fields = ('name', 'year', 'genre__slug', 'category__slug')
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesSerializer
        return CreateTitleSerializer
