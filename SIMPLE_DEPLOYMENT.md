# Simple PythonAnywhere Deployment (SQLite) - Django Travel Booking App

## Quick & Easy Deployment (No Database Setup Required)

This guide shows you how to deploy your Django travel booking app to PythonAnywhere using SQLite database - no MySQL configuration needed!

## Prerequisites
1. PythonAnywhere account (free account works)
2. Your code uploaded to GitHub

## Step-by-Step Simple Deployment

### 1. Upload Your Code to PythonAnywhere

#### A. Open a Bash Console on PythonAnywhere
- Go to your PythonAnywhere dashboard
- Click on "Consoles" → "Bash"

#### B. Clone Your Repository
```bash
git clone https://github.com/fister12/TravelBookingWebsite.git
cd TravelBookingWebsite
```

#### C. Create and Activate Virtual Environment
```bash
python3.10 -m venv travel_env
source travel_env/bin/activate
```

#### D. Install Django (Simple Requirements)
```bash
pip install Django
```

### 2. Simple Database Setup (SQLite - No Configuration!)

#### A. Run Migrations (Uses SQLite by Default)
```bash
cd travel_project
python manage.py migrate
```

#### B. Create Superuser
```bash
python manage.py createsuperuser
```

#### C. Create Sample Data
```bash
python manage.py create_sample_data
```

#### D. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 3. Web App Configuration

#### A. Create Web App
1. Go to PythonAnywhere Dashboard → Web
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10

#### B. Configure WSGI File
1. In the Web tab, find the "Code" section
2. Click on the WSGI configuration file link (usually `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
3. Replace ALL contents with:

```python
#!/usr/bin/env python

import os
import sys

# Add your project directory to sys.path
path = '/home/yourusername/TravelBookingWebsite/travel_project'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_project.settings')

# Import Django
import django
django.setup()

# Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### C. Set Virtual Environment
1. In the Web tab, find "Virtualenv" section
2. Enter: `/home/yourusername/travel_env`

#### D. Configure Static Files
1. In the Web tab, find "Static files" section
2. Add:
   - URL: `/static/`
   - Directory: `/home/yourusername/TravelBookingWebsite/travel_project/static`

#### E. Update Settings for Production
1. In the Web tab, find "Code" section
2. Set "Source code" to: `/home/yourusername/TravelBookingWebsite/travel_project`
3. Set "Working directory" to: `/home/yourusername/TravelBookingWebsite/travel_project`

### 4. Update Django Settings for PythonAnywhere

Edit `travel_project/settings.py` directly (add these lines at the end):

```python
# PythonAnywhere specific settings
import os

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']

# Static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Disable debug in production (optional but recommended)
# DEBUG = False  # Uncomment this line once everything is working
```

### 5. Final Steps

#### A. Reload Web App
Click the green "Reload" button in the Web tab

#### B. Test Your Application
Visit: `https://yourusername.pythonanywhere.com`

## What You Need to Replace

Before deploying, replace `yourusername` with your actual PythonAnywhere username in:
1. The WSGI file paths
2. The static files directory path
3. The ALLOWED_HOSTS setting
4. The virtual environment path

## Complete Example Paths (Replace 'myusername' with yours)

- WSGI file paths: `/home/myusername/TravelBookingWebsite/travel_project`
- Virtual environment: `/home/myusername/travel_env`
- Static files: `/home/myusername/TravelBookingWebsite/travel_project/static`
- Website URL: `https://myusername.pythonanywhere.com`

## Advantages of This Simple Approach

✅ **No database setup required** - SQLite works out of the box  
✅ **Faster deployment** - Skip MySQL configuration  
✅ **Perfect for development/testing** - Get online quickly  
✅ **Free account friendly** - Works with PythonAnywhere free tier  
✅ **Easy to update** - Simple git pull and reload  

## Limitations of SQLite Approach

⚠️ **File-based database** - Stored as a file in your project  
⚠️ **Single connection** - Not ideal for high traffic  
⚠️ **Limited scalability** - Good for small to medium apps  
⚠️ **Backup considerations** - Need to backup the db.sqlite3 file  

## Troubleshooting

### Common Issues:

**Issue: "DisallowedHost" error**
- Solution: Add your PythonAnywhere domain to ALLOWED_HOSTS in settings.py

**Issue: Static files not loading**
- Solution: Run `python manage.py collectstatic` and check static files mapping

**Issue: Module not found**
- Solution: Check virtual environment path in Web tab

**Issue: WSGI errors**
- Solution: Check file paths in WSGI configuration

### Quick Debug Commands:
```bash
# Check if Django can start
python manage.py check

# Test collect static
python manage.py collectstatic --dry-run

# View current directory and files
pwd && ls -la
```

## Updating Your App

When you make changes:
1. SSH into PythonAnywhere or use console
2. Navigate to project: `cd TravelBookingWebsite`
3. Pull changes: `git pull origin main`
4. Activate environment: `source ../travel_env/bin/activate`
5. Run migrations (if needed): `cd travel_project && python manage.py migrate`
6. Collect static files (if needed): `python manage.py collectstatic --noinput`
7. Reload web app from Web tab

## Ready to Go Live?

Once everything is working with SQLite, you can always upgrade to MySQL later by:
1. Creating a MySQL database on PythonAnywhere
2. Updating settings to use MySQL
3. Running `python manage.py migrate` with new settings
4. Transferring data if needed

This simple approach gets you online fast and lets you test everything before dealing with database complexities!
