from django.db import models
from django.contrib.auth.models import AbstractUser

# This is the custom user model class that will be used to create a user
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username or self.full_name
