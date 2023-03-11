from rest_framework import serializers

from .models import Title, Genre, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Title
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = [
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        ]
>>>>>>> 7b581ab9b68c37a407762fa36e330b4d1cc63332


class CreateTitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        slug_field='slug',
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Title
        fields = '__all__'

    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        category_data = validated_data.pop('category')
        title = Title.objects.create(**validated_data, category=category_data)
        for genre_data in genres_data:
            genre = Genre.objects.get(slug=genre_data.slug)
            title.genre.add(genre)
        return title

    def to_representation(self, instance):
        serializer = TitlesSerializer(instance)
        return serializer.data
