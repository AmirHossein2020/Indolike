from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import CartItemSerializer

# Create your views here.
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
