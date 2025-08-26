from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class TravelOption(models.Model):
    TRAVEL_TYPE_CHOICES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]
    
    travel_type = models.CharField(max_length=10, choices=TRAVEL_TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.travel_type} from {self.source} to {self.destination}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    num_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')
    
    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.num_seats) * self.travel_option.price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Booking for {self.user.username} on {self.travel_option}"
