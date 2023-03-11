from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.HiddenField(default=None)

    def validate_title(self, _):
        title = self.context['title']
        if self.context['request'].user.reviews.filter(title=title).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв к этому произведению.'
            )
        return title

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)
