from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import PageNumberPagination

from users.permissions import IsAdminOrReadOnly


class CustomSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
