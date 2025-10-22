from django.db import models
from accounts.models import CustomUser as User


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



class OnlineMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='online_versions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video_file = models.FileField(upload_to='movies/online/', null=True, blank=True)

    def __str__(self):
        return f"{self.movie.name} (Online)"


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls')
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField(default=10)
    seats_per_row = models.PositiveIntegerField(default=12)

    def __str__(self):
        return f"{self.cinema.name} - {self.name}"



class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.movie.name} - {self.hall.name} @ {self.start_time}"



class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=2)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.row}{self.number} ({self.hall.name})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='bookings')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('showtime', 'seat')  # prevent double booking

    def __str__(self):
        return f"{self.user.username} - {self.showtime} - Seat {self.seat}"
