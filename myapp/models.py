from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.username