from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from .models import TravelOption, Booking
from .forms import UserRegisterForm, TravelSearchForm
from datetime import datetime

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def travel_option_list(request):
    travel_options = TravelOption.objects.filter(available_seats__gt=0)
    form = TravelSearchForm(request.GET or None)
    
    if form.is_valid():
        source = form.cleaned_data.get('source')
        destination = form.cleaned_data.get('destination')
        departure_date = form.cleaned_data.get('departure_date')
        
        if source:
            travel_options = travel_options.filter(source__icontains=source)
        if destination:
            travel_options = travel_options.filter(destination__icontains=destination)
        if departure_date:
            travel_options = travel_options.filter(departure_time__date=departure_date)
    
    return render(request, 'booking/travel_option_list.html', {
        'travel_options': travel_options,
        'form': form
    })

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)
    
    if request.method == 'POST':
        num_seats = int(request.POST.get('num_seats', 0))
        
        if num_seats <= 0:
            messages.error(request, 'Please enter a valid number of seats.')
        elif num_seats > travel_option.available_seats:
            messages.error(request, f'Only {travel_option.available_seats} seats available.')
        else:
            # Create booking
            booking = Booking(
                user=request.user,
                travel_option=travel_option,
                num_seats=num_seats
            )
            booking.save()
            
            # Update available seats
            travel_option.available_seats -= num_seats
            travel_option.save()
            
            messages.success(request, 'Booking confirmed successfully!')
            return redirect('my_bookings')
    
    return render(request, 'booking/book_travel.html', {
        'travel_option': travel_option
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'
        booking.save()
        
        # Add seats back to travel option
        travel_option = booking.travel_option
        travel_option.available_seats += booking.num_seats
        travel_option.save()
        
        messages.success(request, 'Booking cancelled successfully!')
    else:
        messages.error(request, 'This booking has already been cancelled.')
    
    return redirect('my_bookings')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')
