from django.contrib import admin
from .models import Movie, OnlineMovie, Cinema, Hall, ShowTime, Seat, Booking
# Register your models here.

admin.site.register(Movie)
admin.site.register(OnlineMovie)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(ShowTime)
admin.site.register(Seat)
admin.site.register(Booking)


