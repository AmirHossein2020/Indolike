from django.db import models
from accounts.models import CustomUser as User

# This is the website model class that will be used to create a website and its related models
class About(models.Model):
    description = models.TextField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.address


# This is the contact model class that will be used to create a contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# This is the movie model class that will be used to create a movie
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



# This is the online movie model class that will be used to create an online movie
class OnlineMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='online_versions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video_file = models.FileField(upload_to='movies/online/', null=True, blank=True)

    def __str__(self):
        return f"{self.movie.name} (Online)"


# This is the cinema model class that will be used to create a cinema
class Cinema(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# This is the hall model class that will be used to create a hall
class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls')
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField(default=10)
    seats_per_row = models.PositiveIntegerField(default=12)

    def __str__(self):
        return f"{self.cinema.name} - {self.name}"



# This is the showtime model class that will be used to create a showtime
class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.movie.name} - {self.hall.name} @ {self.start_time}"


# This is the seat model class that will be used to create a seat
class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=2)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.row}{self.number} ({self.hall.name})"


# This is the booking model class that will be used to create a booking
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

