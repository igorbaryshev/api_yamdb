from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

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
        return self.title.reviews.order_by('id')

    def perform_create(self, serializer):
        title = self.title
        author = self.request.user

        if author.reviews.filter(title=title).exists():
            raise ValidationError('Вы уже делали отзыв к этому произведению.')

        serializer.save(author=author, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    @property
    def review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.review.comments.order_by('id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.review)
