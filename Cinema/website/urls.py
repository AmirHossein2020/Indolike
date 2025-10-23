from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from website.views import *

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
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/showtimes/<int:showtime_id>/seats/', SeatListView.as_view(), name='seat-list'),
    path('api/reserve-seat/', ReserveSeatView.as_view(), name='reserve-seat'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
