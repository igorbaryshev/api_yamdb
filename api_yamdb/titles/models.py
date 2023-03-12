from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=256,
    )
    year = models.PositiveIntegerField(
        'Год выпуска',
        validators=[MaxValueValidator(date.today().year)],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанры',
        related_name='titles',
    )
    description = models.TextField(
        'Описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
