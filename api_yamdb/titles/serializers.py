from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Title, Genre, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = SlugRelatedField(
        many=True, slug_field="slug", queryset=Genre.objects.all()
    )
    category = SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title
