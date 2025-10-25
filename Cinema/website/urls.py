from django.urls import path, include
from rest_framework import routers 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from website.views import * 
from cart.views import *

router = DefaultRouter()
router.register('online-movies', OnlineMovieViewSet, basename='online-movie')


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'online-movies', views.OnlineMovieViewSet)
router.register(r'cinemas', views.CinemaViewSet)
router.register(r'halls', views.HallViewSet)
router.register(r'showtimes', views.ShowTimeViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('api/about/', views.AboutView.as_view(), name='about'),
    path('api/contact/', views.ContactCreateView.as_view(), name='contact'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/showtimes/<int:showtime_id>/seats/', SeatListView.as_view(), name='seat-list'),
    path('api/reserve-seat/', ReserveSeatView.as_view(), name='reserve-seat'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/cart/', CartListView.as_view(), name='cart-list'),
    path('api/cart/add/<int:movie_id>/', AddToCartView.as_view(), name='cart-add'),
    path('api/cart/remove/<int:movie_id>/', RemoveFromCartView.as_view(), name='cart-remove'),
    path('api/cart/checkout/', CheckoutView.as_view(), name='cart-checkout'),
]
