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

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    name = models.CharField(
        verbose_name=('название'),
        max_length=256,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        verbose_name=('слаг'),
    )

    class Meta:
        verbose_name = ('жанр')
        verbose_name_plural = ('жанры')

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='название произведения',
        max_length=256,
    )
    year = models.PositiveIntegerField(
        verbose_name='год выпуска',
        validators=[MaxValueValidator(date.today().year)],
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='категория',
        related_name='titles',
    )
    genre = models.ManyToManyField(
        'Genre',
        blank=True,
        verbose_name='жанры',
        related_name='titles',
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return self.name
