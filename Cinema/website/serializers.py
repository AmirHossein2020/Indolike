from rest_framework import serializers
from .models import Movie, OnlineMovie, Cinema, Hall, ShowTime, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class OnlineMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = OnlineMovie
        fields = '__all__'


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
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    showtime = ShowTimeSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
