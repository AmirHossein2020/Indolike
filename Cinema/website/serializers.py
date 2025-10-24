from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'image', 'duration', 'release_date']


class OnlineMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = OnlineMovie
        fields = ['id', 'movie', 'price', 'video_file']

        
    def get_purchased(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return OnlinePurchase.objects.filter(user=user, online_movie=obj).exists()
        return False

class OnlinePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlinePurchase
        fields = ['id', 'user', 'online_movie', 'purchased_at']


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)
    class Meta:
        model = Hall
        fields = '__all__'


class ShowTimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    hall = HallSerializer(read_only=True)

    class Meta:
        model = ShowTime
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    is_reserved = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['id', 'row', 'number', 'hall', 'is_reserved']

    def get_is_reserved(self, obj):
        showtime_id = self.context.get('showtime_id')
        if not showtime_id:
            return False
     
        return Booking.objects.filter(seat=obj, showtime_id=showtime_id).exists()

class BookingSerializer(serializers.ModelSerializer):
    showtime = ShowTimeSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='online_movie.movie.name', read_only=True)
    price = serializers.DecimalField(source='online_movie.price', max_digits=10, decimal_places=2, read_only=True)
    image = serializers.ImageField(source='online_movie.movie.image', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'movie_name', 'price', 'image', 'added_at', 'online_movie']