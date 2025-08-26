#!/bin/bash

# PythonAnywhere Deployment Script for Django Travel Booking App
# Run this script after uploading your code to PythonAnywhere

echo "🚀 Starting Django Travel Booking App deployment on PythonAnywhere..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Make sure you're in the project root directory."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source ../travel_env/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if production settings exist
if [ ! -f "travel_project/production_settings.py" ]; then
    echo "❌ Error: production_settings.py not found. Please create it first."
    exit 1
fi

# Run migrations
echo "🗃️  Running database migrations..."
python manage.py migrate --settings=travel_project.production_settings

# Create superuser (optional - will prompt)
echo "👤 Do you want to create a superuser? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser --settings=travel_project.production_settings
fi

# Create sample data (optional)
echo "📊 Do you want to create sample travel data? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py create_sample_data --settings=travel_project.production_settings
fi

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --settings=travel_project.production_settings

# Check for common issues
echo "🔍 Running system checks..."
python manage.py check --settings=travel_project.production_settings

echo "✅ Deployment script completed!"
echo ""
echo "📋 Next steps:"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Configure WSGI file"
echo "3. Set virtual environment path"
echo "4. Configure static files mapping"
echo "5. Reload your web app"
echo "6. Visit your site: https://yourusername.pythonanywhere.com"
echo ""
echo "📖 For detailed instructions, see PYTHONANYWHERE_DEPLOYMENT.md"
