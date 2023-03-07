from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Жанр'
    )
    slug = models.SlugField()

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
        related_name='title'
    )
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
