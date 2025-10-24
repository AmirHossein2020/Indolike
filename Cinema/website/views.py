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

class BuyOnlineMovieView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, movie_id):
        movie = OnlineMovie.objects.get(id=movie_id)
        purchase, created = OnlinePurchase.objects.get_or_create(
            user=request.user, movie=movie
        )
        if not created:
            return Response({"detail": "You already own this movie."}, status=400)
        return Response({"detail": "Purchase successful."}, status=200)

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

class CartListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, movie_id):
        try:
            movie = OnlineMovie.objects.get(pk=movie_id)
        except OnlineMovie.DoesNotExist:
            return Response({'detail': 'Movie not found.'}, status=404)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, online_movie=movie)
        if not created:
            return Response({'detail': 'Movie already in cart.'}, status=400)

        return Response({'detail': 'Movie added to cart.'}, status=201)


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, movie_id):
        try:
            item = CartItem.objects.get(user=request.user, online_movie_id=movie_id)
            item.delete()
            return Response({'detail': 'Removed from cart.'})
        except CartItem.DoesNotExist:
            return Response({'detail': 'Item not found in cart.'}, status=404)


class CheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'detail': 'Cart is empty.'}, status=400)

        for item in cart_items:
            OnlinePurchase.objects.get_or_create(
                user=request.user, online_movie=item.online_movie
            )
        cart_items.delete()
        return Response({'detail': 'Checkout successful. Movies purchased!'})
