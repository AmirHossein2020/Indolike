from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# This CustomUser model extends the default Django user model to include additional fields.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)