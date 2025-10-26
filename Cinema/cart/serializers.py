from rest_framework import serializers
from .models import CartItem

# This is the serializer class that will be used to serialize the cart item model
class CartItemSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='online_movie.movie.name', read_only=True)
    price = serializers.DecimalField(source='online_movie.price', max_digits=10, decimal_places=2, read_only=True)
    image = serializers.ImageField(source='online_movie.movie.image', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'movie_name', 'price', 'image', 'added_at', 'online_movie']