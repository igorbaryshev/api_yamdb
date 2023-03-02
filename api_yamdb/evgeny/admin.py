from django.contrib import admin

from .models import Title, Category, Genre


@admin.register(Title)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year')

@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

