from django.db import models
from accounts.models import CustomUser

class Nbook(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='notebook/images/', null=True, blank=True)
    filenotebook = models.FileField(upload_to='notebook/files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def get_short_text(self):
        return self.text[:100] + "..." if len(self.text) > 100 else self.text
