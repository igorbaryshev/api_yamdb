from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Категория'
    )
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Genre(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Жанр'
    )
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название произведения',
    )
    year = models.IntegerField()
    category = models.ForeignKey(
        Category,
        null=True,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='title'
    )
    
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        null=True,
        related_name='title'
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'