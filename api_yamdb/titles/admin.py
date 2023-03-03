from django.contrib import admin

from .models import Title, Category, Genre


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
