from django.urls import path, include
from rest_framework import routers
from . import views

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
]
