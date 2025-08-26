from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_option_list, name='travel_option_list'),
    path('register/', views.register, name='register'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile, name='profile'),
]
