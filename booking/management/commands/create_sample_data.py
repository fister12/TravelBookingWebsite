from django.core.management.base import BaseCommand
from booking.models import TravelOption
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Create sample travel options for testing'

    def handle(self, *args, **options):
        # Clear existing data
        TravelOption.objects.all().delete()
        
        # Sample cities
        cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
                 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
                 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte']
        
        travel_types = ['Flight', 'Train', 'Bus']
        
        # Create sample travel options
        for i in range(50):
            source = random.choice(cities)
            destination = random.choice([city for city in cities if city != source])
            travel_type = random.choice(travel_types)
            
            # Generate random departure time (next 30 days)
            departure_time = datetime.now() + timedelta(
                days=random.randint(1, 30),
                hours=random.randint(6, 23),
                minutes=random.choice([0, 15, 30, 45])
            )
            
            # Set prices based on travel type
            if travel_type == 'Flight':
                price = random.randint(150, 800)
            elif travel_type == 'Train':
                price = random.randint(80, 300)
            else:  # Bus
                price = random.randint(25, 150)
            
            available_seats = random.randint(10, 50)
            
            TravelOption.objects.create(
                travel_type=travel_type,
                source=source,
                destination=destination,
                departure_time=departure_time,
                price=price,
                available_seats=available_seats
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created 50 sample travel options')
        )
