from rest_framework import serializers


from .models import Title, Genre, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category
