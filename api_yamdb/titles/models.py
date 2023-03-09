from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Категория',
    )
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Жанр',
    )
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения',
    )
    year = models.PositiveIntegerField(validators=[
        MaxValueValidator(date.today().year),
    ])
    category = models.ForeignKey(
        Category,
        null=True,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
    )
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
