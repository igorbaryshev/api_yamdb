from django_filters.rest_framework import DjangoFilterBackend


class GenreFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        genre = request.query_params.get('genre')
        category = request.query_params.get('category')
        if genre is not None:
            return queryset.filter(genre__slug=genre)
        if category is not None:
            return queryset.filter(category__slug=category)
        return queryset
