from rest_framework import viewsets
from .models import Movie, OnlineMovie, Cinema, Hall, ShowTime, Seat, Booking
from .serializers import (
    MovieSerializer,
    OnlineMovieSerializer,
    CinemaSerializer,
    HallSerializer,
    ShowTimeSerializer,
    SeatSerializer,
    BookingSerializer
)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class OnlineMovieViewSet(viewsets.ModelViewSet):
    queryset = OnlineMovie.objects.all()
    serializer_class = OnlineMovieSerializer


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class ShowTimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
