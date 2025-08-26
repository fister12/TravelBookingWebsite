#!/bin/bash

# Simple PythonAnywhere Deployment Script (SQLite)
# Run this script in your project directory on PythonAnywhere

echo "🚀 Starting SIMPLE deployment to PythonAnywhere..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Make sure you're in the travel_project directory."
    exit 1
fi

# Install Django (simple approach)
echo "📦 Installing Django..."
pip install Django

# Run migrations (creates SQLite database automatically)
echo "🗃️  Setting up database..."
python manage.py migrate

# Create superuser
echo "👤 Create a superuser account:"
python manage.py createsuperuser

# Create sample data
echo "📊 Creating sample travel data..."
python manage.py create_sample_data

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Run basic checks
echo "🔍 Running system checks..."
python manage.py check

echo ""
echo "✅ Simple deployment completed!"
echo ""
echo "📋 Next steps:"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Create a new web app (Manual configuration, Python 3.10)"
echo "3. Update WSGI file with the provided configuration"
echo "4. Set virtual environment path"
echo "5. Add static files mapping: /static/ → /home/yourusername/TravelBookingWebsite/travel_project/static"
echo "6. Reload your web app"
echo "7. Visit: https://yourusername.pythonanywhere.com"
echo ""
echo "📖 For detailed instructions, see SIMPLE_DEPLOYMENT.md"
