# Django Travel Booking Application

A comprehensive web application for booking travel options including flights, trains, and buses. Built with Django and styled with Bootstrap 5.

## Features

- **User Authentication**: Registration, login, and logout functionality
- **Travel Search**: Search for travel options by source, destination, and departure date
- **Booking Management**: Book tickets, view bookings, and cancel bookings
- **Admin Panel**: Manage travel options and bookings through Django admin
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5

## Models

### TravelOption
- `travel_type`: Flight, Train, or Bus
- `source`: Source city
- `destination`: Destination city
- `departure_time`: Departure date and time
- `price`: Price per seat
- `available_seats`: Number of available seats

### Booking
- `user`: User who made the booking
- `travel_option`: Selected travel option
- `num_seats`: Number of seats booked
- `total_price`: Automatically calculated total price
- `booking_date`: When the booking was made
- `status`: Confirmed or Cancelled

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd travel_project
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv travel_env
travel_env\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv travel_env
source travel_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### For Regular Users
1. Register a new account or login with existing credentials
2. Browse available travel options on the home page
3. Use the search form to filter by source, destination, or departure date
4. Click "Book Now" to book a travel option
5. View your bookings in "My Bookings"
6. Cancel bookings if needed

### For Administrators
1. Access the admin panel at `/admin/`
2. Add new travel options
3. Manage user bookings
4. View booking statistics

## Project Structure

```
travel_project/
├── booking/
│   ├── migrations/
│   ├── templates/
│   │   ├── booking/
│   │   │   ├── base.html
│   │   │   ├── travel_option_list.html
│   │   │   ├── book_travel.html
│   │   │   └── my_bookings.html
│   │   └── registration/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── profile.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── travel_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Key URLs

- `/` - Home page with travel options
- `/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/book/<id>/` - Book a specific travel option
- `/my-bookings/` - View user's bookings
- `/booking/cancel/<id>/` - Cancel a booking
- `/profile/` - User profile
- `/admin/` - Admin panel

## Technologies Used

- **Backend**: Django 5.x
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (when available)
5. Submit a pull request

## License

This project is for educational purposes.
