from django_filters import rest_framework as filters
from .models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(method='filter_by_genre')
    category = filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Title
        fields = ['year', 'name']

    def filter_by_genre(self, queryset, name, value):
        return queryset.filter(genre__slug=value)

    def filter_by_category(self, queryset, name, value):
        return queryset.filter(category__slug=value)
