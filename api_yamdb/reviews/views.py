from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# from rest_framework.exceptions import ValidationError

from users.permissions import IsAuthorOrReadOnly
from reviews.models import Review
from titles.models import Title
from reviews.serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    @property
    def title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.title.reviews.order_by('pub_date')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['title'] = self.title
        return context

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
