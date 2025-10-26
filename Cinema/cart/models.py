from django.db import models
from accounts.models import CustomUser as User
from website.models import OnlineMovie
# Create your models here.

# This is the online purchase model class
class OnlinePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    online_movie = models.ForeignKey(OnlineMovie, on_delete=models.CASCADE, related_name='purchases')
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'online_movie')

    def __str__(self):
        return f"{self.user.username} bought {self.online_movie.movie.name}"


# This is the cart item model class 
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    online_movie = models.ForeignKey(OnlineMovie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'online_movie')

    def __str__(self):
        return f"{self.user.username} - {self.online_movie.movie.name}"
