from django.db import models
from django.utils.crypto import get_random_string

# The ShortURL model stores original URLs and their corresponding short codes.
class ShortURL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = get_random_string(6)  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
