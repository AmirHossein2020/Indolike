from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .models import Seat
from .serializers import  BookingSerializer



class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password:
            return Response({"error": "Username and password required."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)

        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "User registered successfully!",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)




class SeatListView(generics.ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        showtime_id = self.kwargs['showtime_id']
        showtime = ShowTime.objects.get(id=showtime_id)
        return Seat.objects.filter(hall=showtime.hall).order_by('row', 'number')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['showtime_id'] = self.kwargs['showtime_id']
        return context
    
class ReserveSeatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        seat_id = request.data.get("seat_id")
        showtime_id = request.data.get("showtime_id")

        if not seat_id or not showtime_id:
            return Response({"detail": "Seat or showtime missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            seat = Seat.objects.get(id=seat_id)
            showtime = ShowTime.objects.get(id=showtime_id)
        except (Seat.DoesNotExist, ShowTime.DoesNotExist):
            return Response({"detail": "Seat or showtime not found"}, status=status.HTTP_404_NOT_FOUND)

   
        if Booking.objects.filter(seat=seat, showtime=showtime).exists():
            return Response({"detail": "Seat already reserved"}, status=status.HTTP_400_BAD_REQUEST)

   
        Booking.objects.create(user=user, seat=seat, showtime=showtime)
        seat.is_reserved = True
        seat.save()

        return Response({"detail": "Seat reserved successfully"})
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class OnlineMovieViewSet(viewsets.ModelViewSet):
    queryset = OnlineMovie.objects.all()
    serializer_class = OnlineMovieSerializer
    permission_classes = [permissions.AllowAny]


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





