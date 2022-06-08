"""
Module to define models related customized authentication app.
"""
from django.contrib.auth. models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Customized User model."""

    class UserRole(models.TextChoices):
        """User role model."""

        CREATOR = ('Créateur', 'CREATOR')
        SUBSCRIBER = ('Abonné', 'SUBSCRIBER')

    profile_photo = models.ImageField("Photo de profil")
    role = models.CharField("Role", max_length=30, choices=UserRole.choices)

