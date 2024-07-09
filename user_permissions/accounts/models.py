from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    field = models.EmailField(max_length=255, unique=False, default='unknown')
    name = models.CharField(max_length=255, default='unknown')

    def __str__(self):
        return self.username
