from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    bio = models.TextField(blank=True)

    role = models.CharField(
        max_length=32,
        choices=Role.choices,
        default=Role.USER
    )
